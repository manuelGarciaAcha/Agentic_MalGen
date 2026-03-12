from dataclasses import dataclass, field
from typing import List, Dict, Optional, Literal

@dataclass
class FixItem:
    id: str # identifier for runner control/iteration management
    title: str
    instruction: str
    severity: str # classifiers such as major, minor, etc
    status: Literal["open", "fixed", "partial", "not_fixed"] = "open"

@dataclass
class Draft:
    output: str
    notes: str
    applied_fixes: List[str] # FixItems IDs, if any
    iterations: int

@dataclass
class ReviewResult:
    overall_score: int
    subscores: Dict[str,int]
    issues: List[FixItem] = field(default_factory=list)
    summary: str = ""


GENERATOR_FORMAT_ERR = "ERROR: Generator Format Error"
GENERATOR_JSON_ERR = "ERROR: Generator JSON error"
REVIEWER_FORMAT_ERR = "ERROR: Reviewer Format Error"
REVIEWER_JSON_ERR = "ERROR: Reviewer JSON Error"
RETRY_FIRST_ITERATION = "Re-attempt first generation"
