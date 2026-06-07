"""
graph.py — LangGraph graph definition for the agentic malware generation system.

Graph topology:

    [START]
       |
    [planner]          # Decomposes raw prompt into structured MalSpec
       |
    [generator]        # Generates Python code from MalSpec
       |
    [reviewer]         # Evaluates code against MalSpec
       |
    <route_after_review>
       |-- "regenerate" --> [generator]   (score < 7, issues exist, under max_iter)
       |-- "evasion"    --> [evasion_analyst]  (passed review)
       |-- "end"        --> [END]         (max iterations reached without passing)
       |
    [evasion_analyst]  # Analyzes final code for detectable patterns
       |
    [END]

Key design decisions:
  1. Typed state (MalGenState) replaces freeform JSON inter-agent comms.
  2. Pydantic schema validation in model.py replaces raw JSON parsing.
  3. Planner node separates task decomposition from code generation.
  4. Evasion Analyst runs post-convergence, keeping review concerns separate.
  5. Conditional edge logic mirrors the original Runner's loop conditions
     (continue if issues exist OR score < 7, stop at max_iterations).
"""

from langgraph.graph import StateGraph, START, END

from core.state import MalGenState
from agents.planner import planner_node
from agents.generator import generator_node
from agents.reviewer import reviewer_node
from agents.evasion_analyst import evasion_analyst_node


# --- Conditional edge routing function ---

def route_after_review(state: MalGenState) -> str:
    """
    Routing logic — mirrors the original Runner's loop conditions:
      - If max iterations reached: end (regardless of score)
      - If passed review (score >= 7, no issues, syntax valid): go to evasion
      - Otherwise: regenerate

    The original system used:
      if iteration < max_iterations AND (issues exist OR score < 7): continue
    We express the same logic inverted for clarity.
    """
    if state["max_iterations_reached"]:
        return "end"
    if state["passed_review"]:
        return "evasion"
    return "regenerate"


# --- Graph construction ---

def build_graph() -> StateGraph:
    graph = StateGraph(MalGenState)

    # Add nodes
    graph.add_node("planner", planner_node)
    graph.add_node("generator", generator_node)
    graph.add_node("reviewer", reviewer_node)
    graph.add_node("evasion_analyst", evasion_analyst_node)

    # Linear edges
    graph.add_edge(START, "planner")
    graph.add_edge("planner", "generator")
    graph.add_edge("generator", "reviewer")

    # Conditional edge after reviewer
    graph.add_conditional_edges(
        "reviewer",
        route_after_review,
        {
            "regenerate": "generator",
            "evasion": "evasion_analyst",
            "end": END,
        },
    )

    # Evasion analyst always terminates
    graph.add_edge("evasion_analyst", END)

    return graph


def compile_graph():
    """Returns a compiled, runnable LangGraph app."""
    return build_graph().compile()
