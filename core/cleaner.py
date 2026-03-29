import ast
import re


def extract_code_from_response(response: str) -> str:
    """Extract only executable Python code from an LLM response.

    Works regardless of whether the model followed instructions.
    Handles: markdown fences, preamble prose, inline comments,
    docstrings, trailing explanations, and mixed code/text output.
    """
    code = _try_extract_fenced_block(response)
    if code is None:
        code = _try_extract_by_line_analysis(response)
    code = _strip_comments(code)
    code = _strip_docstrings(code)
    code = _strip_blank_runs(code)
    code = _fix_unmatched_parens(code)
    return code.strip()


def _try_extract_fenced_block(text: str) -> str | None:
    """If the response contains ```python or ``` fenced code, extract it."""
    pattern = r"```(?:python|py)?\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return "\n".join(matches)
    return None


def _try_extract_by_line_analysis(text: str) -> str:
    """For responses without fences, keep only lines that look like Python code."""
    lines = text.split("\n")
    code_lines = []
    in_code = False

    for line in lines:
        stripped = line.strip()
        if _is_code_line(stripped):
            in_code = True
            code_lines.append(line)
        elif in_code and stripped == "":
            code_lines.append("")
        elif in_code and _is_prose(stripped):
            in_code = False
        elif in_code:
            code_lines.append(line)

    return "\n".join(code_lines)


def _is_code_line(line: str) -> bool:
    """Heuristic: does this line look like Python code?"""
    if line == "":
        return False
    code_starters = (
        "import ",
        "from ",
        "def ",
        "class ",
        "if ",
        "elif ",
        "else:",
        "for ",
        "while ",
        "try:",
        "except",
        "finally:",
        "with ",
        "return ",
        "yield ",
        "raise ",
        "pass",
        "break",
        "continue",
        "print(",
        "open(",
        "os.",
        "sys.",
        "@",
    )
    if line.startswith(code_starters):
        return True
    if re.match(r"^[a-zA-Z_]\w*\s*[=(]", line):
        return True
    if re.match(
        r"^\s+(import |from |def |class |if |elif |else:|for |while |"
        r"try:|except|finally:|with |return |yield |raise |pass|break|"
        r"continue|print\(|open\(|[a-zA-Z_]\w*\s*[=(]|#|\))",
        line,
    ):
        return True
    if re.match(r"^\s+\S", line):
        return True
    return False


def _is_prose(line: str) -> bool:
    """Heuristic: does this line look like natural language, not code?"""
    if line.startswith(("#", "import ", "from ", "def ", "class ")):
        return False
    prose_patterns = [
        r"^(Here|This|The|Note|I |You |We |It |As |In |To |For |A |An )",
        r"^(Sure|Certainly|Of course|Let me|Below|Above|Following)",
        r"^(Output|Result|Example|Explanation|Summary|Step \d)",
        r"^\d+\.\s+\w",
        r"^[-*]\s+\w",
    ]
    for pat in prose_patterns:
        if re.match(pat, line, re.IGNORECASE):
            return True
    return False


def _strip_comments(code: str) -> str:
    """Remove all comment-only lines. Preserve inline code before #."""
    lines = code.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if "#" in line:
            in_string = False
            quote_char = None
            cut_idx = None
            i = 0
            while i < len(line):
                ch = line[i]
                if not in_string and ch in ('"', "'"):
                    if line[i : i + 3] in ('"""', "'''"):
                        in_string = True
                        quote_char = line[i : i + 3]
                        i += 3
                        continue
                    in_string = True
                    quote_char = ch
                elif in_string:
                    if len(quote_char) == 3 and line[i : i + 3] == quote_char:
                        in_string = False
                        i += 3
                        continue
                    elif (
                        len(quote_char) == 1
                        and ch == quote_char
                        and line[i - 1 : i] != "\\"
                    ):
                        in_string = False
                elif ch == "#":
                    cut_idx = i
                    break
                i += 1
            if cut_idx is not None:
                result.append(line[:cut_idx].rstrip())
            else:
                result.append(line)
        else:
            result.append(line)
    return "\n".join(result)


def _strip_docstrings(code: str) -> str:
    """Remove triple-quoted docstrings."""
    code = re.sub(r'""".*?"""', "", code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", "", code, flags=re.DOTALL)
    return code


def _strip_blank_runs(code: str) -> str:
    """Collapse runs of 3+ blank lines down to 1."""
    return re.sub(r"\n{3,}", "\n\n", code)


def _fix_unmatched_parens(code: str) -> str:
    """Fix lines with more closing parens/brackets than opening ones.

    Small models like stable-code frequently produce f.write(str(key)))
    instead of f.write(str(key)). Fix this line-by-line.
    """
    lines = code.split("\n")
    fixed = []
    for line in lines:
        content = line.lstrip()
        indent = line[: len(line) - len(content)]

        for open_ch, close_ch in [("(", ")"), ("[", "]"), ("{", "}")]:
            opens = content.count(open_ch)
            closes = content.count(close_ch)
            while closes > opens:
                idx = content.rfind(close_ch)
                content = content[:idx] + content[idx + 1 :]
                closes -= 1

        fixed.append(indent + content)
    return "\n".join(fixed)


def validate_syntax(code: str) -> tuple[bool, str]:
    """Check if the cleaned code is valid Python syntax."""
    try:
        ast.parse(code)
        return True, ""
    except SyntaxError as e:
        return False, f"Line {e.lineno}: {e.msg}"
