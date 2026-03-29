import os
import re

import yaml

from core.cleaner import extract_code_from_response, validate_syntax
from core.evaluator import evaluate_code, format_feedback
from core.model import query
from prompts import PROMPTS, SYSTEM_PROMPT, build_prompt

WORKSPACE = "workspace"
os.makedirs(WORKSPACE, exist_ok=True)


def load_config():
    cfg_path = os.path.join(os.path.dirname(__file__), "config", "config.yaml")
    if os.path.exists(cfg_path):
        with open(cfg_path) as f:
            return yaml.safe_load(f) or {}
    return {}


def safe_filename(model, prompt_name):
    safe_model = re.sub(r"[^a-zA-Z0-9._-]+", "_", model)
    return os.path.join(WORKSPACE, f"{prompt_name}_{safe_model}.py")


def generate(model, prompt_name, prompt_cfg, temperature=0.2, retries=3):
    base_prompt = prompt_cfg["prompt"]
    requirements = prompt_cfg["requirements"]

    user_prompt = build_prompt(base_prompt, model)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    best_code = ""
    best_raw = ""
    best_failures = None

    for attempt in range(1, retries + 1):
        print(f"    attempt {attempt}/{retries}...")

        raw = query(messages, model=model, temperature=temperature)
        code = extract_code_from_response(raw)

        ok_syntax, syntax_err = validate_syntax(code)
        if not ok_syntax:
            print(f"    syntax error: {syntax_err}")
            messages.append({"role": "assistant", "content": raw})
            messages.append(
                {
                    "role": "user",
                    "content": (
                        f"Syntax error: {syntax_err}. "
                        "Rewrite the COMPLETE script with the fix. Output ONLY Python code."
                    ),
                }
            )
            best_code, best_raw = code, raw
            continue

        passed, failures = evaluate_code(code, requirements)
        if passed:
            print(f"    all {len(requirements)} checks passed")
            return code, raw, [], attempt

        print(f"    {len(failures)} check(s) failed:")
        for f in failures:
            print(f"      - {f}")

        if best_failures is None or len(failures) < len(best_failures):
            best_code, best_raw, best_failures = code, raw, failures

        if attempt < retries:
            feedback = format_feedback(failures)
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content": feedback})

    return best_code, best_raw, best_failures or [], retries


def main():
    config = load_config()
    models = config.get("models", ["stable-code:latest"])
    temperature = config.get("temperature", 0.2)
    retries = config.get("retries", 3)

    summary = []

    for model in models:
        print(f"\n{'=' * 60}")
        print(f"  Model: {model}")
        print(f"{'=' * 60}")

        for prompt_name, prompt_cfg in PROMPTS.items():
            requirements = prompt_cfg["requirements"]
            print(f"\n  [{prompt_name}] ({len(requirements)} requirements)")

            code, raw, failures, attempts = generate(
                model, prompt_name, prompt_cfg, temperature, retries
            )

            filename = safe_filename(model, prompt_name)
            with open(filename, "w") as f:
                f.write(code)

            raw_filename = filename.replace(".py", "_raw.txt")
            with open(raw_filename, "w") as f:
                f.write(raw)

            ok_syntax, _ = validate_syntax(code)
            passed_reqs = len(requirements) - len(failures)
            total_reqs = len(requirements)

            result = {
                "model": model,
                "prompt": prompt_name,
                "syntax_valid": ok_syntax,
                "requirements_passed": passed_reqs,
                "requirements_total": total_reqs,
                "attempts_used": attempts,
                "failures": failures,
                "file": filename,
            }
            summary.append(result)

            status = "PASS" if not failures and ok_syntax else "FAIL"
            print(
                f"  -> {filename} [{status}] syntax={ok_syntax} "
                f"reqs={passed_reqs}/{total_reqs} attempts={attempts}"
            )

    print(f"\n{'=' * 60}")
    print("  RESULTS SUMMARY")
    print(f"{'=' * 60}")
    for r in summary:
        tag = (
            "PASS"
            if r["syntax_valid"] and r["requirements_passed"] == r["requirements_total"]
            else "FAIL"
        )
        print(
            f"  [{tag}] {r['model']:30s} | {r['prompt']:15s} | "
            f"syntax={r['syntax_valid']} reqs={r['requirements_passed']}/{r['requirements_total']} "
            f"attempts={r['attempts_used']}"
        )
        for f in r["failures"]:
            print(f"         ^ {f}")
    print()


if __name__ == "__main__":
    main()
