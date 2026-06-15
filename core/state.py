"""
MalGenState: Typed LangGraph state for the agentic malware generation system.

Replaces the freeform JSON inter-agent communication (Draft, ReviewResult,
FixItems in the original comms.py) with a single typed TypedDict that
LangGraph carries across all nodes. This eliminates the JSON formatting
failure mode identified as the primary failure cause in the v1 system.
"""

from typing import Annotated, Optional
from typing_extensions import TypedDict
import operator


class MalSpec(TypedDict):
    """Structured task specification produced by the Planner agent."""
    objective: str                  # e.g. "Python keylogger with exfiltration"
    target_os: str                  # e.g. "Windows 10/11"
    required_behaviors: list[str]   # e.g. ["capture keystrokes", "write to file", "transmit over socket"]
    libraries: list[str]            # e.g. ["pynput", "socket"]
    output_format: str              # always "python_only_no_comments"
    constraints: list[str]          # e.g. ["no syntax errors", "no explanatory text"]
    exfil_target: Optional[str]     # IP:port if applicable


class ReviewResult(TypedDict):
    """Structured review output produced by the Reviewer agent."""
    overall_score: int              # 0-10
    issues: list[str]               # list of specific issues found
    resolved_issues: list[str]      # issues marked resolved vs prior iteration
    spec_alignment: bool            # does code meet the MalSpec requirements
    syntax_valid: bool              # passes basic syntax check
    feedback: str                   # free-text feedback for Generator


class EvasionAssessment(TypedDict):
    """Evasion analysis produced by the Evasion Analyst agent."""
    detectable_patterns: list[str]  # e.g. ["bare pynput import", "plaintext file write"]
    evasion_suggestions: list[str]  # e.g. ["alias import", "encode log content"]
    evasion_score: int              # 0-10, higher = more evasive
    modified_code: Optional[str]    # evasion-hardened version of the code


class MalGenState(TypedDict):
    """
    Full graph state carried across all nodes.
    
    LangGraph passes this dict through every node. Each node receives
    the current state and returns a partial update dict — only the
    keys it modifies. LangGraph merges updates via the reducer.
    
    The `messages` field uses operator.add as reducer (append-only),
    giving a full execution trace across iterations without overwriting.
    """
    # --- Input ---
    raw_prompt: str                             # original user prompt (P1-P4 style)
    model_name: str                             # e.g. "codegemma:7b"
    max_iterations: int                         # default 10

    # --- Planner output ---
    spec: Optional[MalSpec]

    # --- Generation loop ---
    current_code: Optional[str]                 # latest generated Python code
    iteration: int                              # current iteration count
    review: Optional[ReviewResult]              # latest review

    # --- Evasion ---
    evasion: Optional[EvasionAssessment]

    # --- Control flags ---
    passed_review: bool                         # True when score >= 7 and no issues
    max_iterations_reached: bool

    # --- Trace log (append-only, full history) ---
    messages: Annotated[list[str], operator.add]
