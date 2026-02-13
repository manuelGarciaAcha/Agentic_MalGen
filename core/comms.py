from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class FixItem:
    id: str # identifier for runner control/iteration management
    title: str
    instruction: str
    severity: str # classifiers such as major, minor, etc

@dataclass
class Draft:
    output: str
    assumptions: str
    applied_fixes: List[str] # FixItems IDs, if any
    iterations: int

@dataclass
class ReviewResult:
    overall_score: float
    subscores: Dict[str,float]
    issues: List[FixItem] = field(default_factory=list)
    fixes: List[FixItem] = field(default_factory=list)
    summary: str = ""
