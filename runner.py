"""
runner.py — Entry point for the LangGraph agentic malware generation system.

Replaces the original runner.py while-loop orchestrator.
LangGraph handles the iteration loop via the compiled graph;
this script handles experiment setup, workspace logging, and
multi-model/multi-prompt batch runs matching the original experiment design.

Usage:
    python runner.py --model codegemma:7b --prompt 1
    python runner.py --model codestral:22b --prompt 4
    python runner.py --batch  # runs all 7 models x 4 prompts
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

from graph import compile_graph
from core.state import MalGenState
from core.prompts import PROMPTS

# Models from the original experiment
MODELS = [
    "yi-coder:9b",
    "codeqwen:7b",
    "qwen2.5-coder:32b",
    "vanilj/trinity-2-codestral-22b-v0.2:4_k_m",
    "codegemma:7b",
    "phind-codellama:34b",
    "codestral:22b",
    "stable-code:3b",
    "deepseek-coder:6.7b",
    "codellama:7b",
]


def initial_state(model_name: str, prompt_key: str) -> MalGenState:
    """Build the initial state for a run."""
    return MalGenState(
        raw_prompt=PROMPTS[prompt_key],
        model_name=model_name,
        max_iterations=10,
        spec=None,
        current_code=None,
        iteration=0,
        review=None,
        evasion=None,
        passed_review=False,
        max_iterations_reached=False,
        messages=[],
    )


def save_run(workspace: Path, final_state: MalGenState, model: str, prompt_key: str):
    """Save full run artifacts to workspace directory — mirrors original output structure."""
    run_dir = workspace / f"{model.replace(':', '_').replace('/', '_')}_PROMPT{prompt_key}"
    run_dir.mkdir(parents=True, exist_ok=True)

    # Final code
    if final_state["current_code"]:
        code_path = run_dir / f"{model.replace(':', '_').replace('/', '_')}_P{prompt_key}_output.py"
        code_path.write_text(final_state["current_code"])

    # Evasion-hardened code
    if final_state.get("evasion") and final_state["evasion"].get("modified_code"):
        evasion_path = run_dir / f"{model.replace(':', '_').replace('/', '_')}_P{prompt_key}_evasion.py"
        evasion_path.write_text(final_state["evasion"]["modified_code"])

    # Full state as JSON
    summary = {
        "model": model,
        "prompt": prompt_key,
        "iterations": final_state["iteration"],
        "passed_review": final_state["passed_review"],
        "max_iterations_reached": final_state["max_iterations_reached"],
        "final_score": final_state["review"]["overall_score"] if final_state.get("review") else None,
        "evasion_score": final_state["evasion"]["evasion_score"] if final_state.get("evasion") else None,
        "spec": final_state.get("spec"),
        "final_review": final_state.get("review"),
        "evasion_assessment": final_state.get("evasion"),
        "trace": final_state["messages"],
        "timestamp": datetime.now().isoformat(),
    }
    (run_dir / "final_output.json").write_text(json.dumps(summary, indent=2))

    print(f"  Saved to {run_dir}")
    return summary


def run_single(model: str, prompt_key: str, workspace: Path) -> dict:
    print(f"\n{'='*60}")
    print(f"Model: {model}  |  Prompt: P{prompt_key}")
    print(f"{'='*60}")

    app = compile_graph()
    state = initial_state(model, prompt_key)

    final_state = app.invoke(state)

    # Print trace
    for msg in final_state["messages"]:
        print(f"  {msg}")

    summary = save_run(workspace, final_state, model, prompt_key)

    print(f"\n  Result: {'PASSED' if summary['passed_review'] else 'FAILED'} "
          f"| Iterations: {summary['iterations']} "
          f"| Review score: {summary['final_score']} "
          f"| Evasion score: {summary['evasion_score']}")

    return summary


def run_batch(workspace: Path):
    results = []
    for model in MODELS:
        for prompt_key in ["1", "2", "3", "4"]:
            try:
                summary = run_single(model, prompt_key, workspace)
                results.append(summary)
            except Exception as e:
                print(f"  ERROR: {model} P{prompt_key}: {e}")
                results.append({
                    "model": model, "prompt": prompt_key,
                    "error": str(e), "passed_review": False,
                })

    # Aggregate results table
    print("\n\nRESULTS SUMMARY")
    print(f"{'Model':<25} {'P1':>6} {'P2':>6} {'P3':>6} {'P4':>6} {'Pass%':>8}")
    print("-" * 60)
    for model in MODELS:
        model_results = [r for r in results if r.get("model") == model]
        scores = []
        for r in sorted(model_results, key=lambda x: x.get("prompt", "0")):
            
            if r.get("error"):
                scores.append("ERR")
            elif r.get("passed_review"):
                scores.append(f"PASSED/R{review_score}/E{evasion_score}")
            else:
                review_score = r.get("final_score", "?")
                evasion_score = r.get("evasion_score", "?")
                scores.append(f"FAIL/R{review_score}/E{evasion_score}")
        pass_count = sum(1 for r in model_results if r.get("passed_review"))
        total = len(model_results)
        print(f"{model:<35} " + " ".join(f"{s:>20}" for s in scores) + f" {pass_count}/{total:>5}")

    (workspace / "batch_results.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="codegemma:7b", choices=MODELS)
    parser.add_argument("--prompt", default="1", choices=["1", "2", "3", "4"])
    parser.add_argument("--batch", action="store_true")
    args = parser.parse_args()

    workspace = Path("test_workspace")
    workspace.mkdir(exist_ok=True)

    if args.batch:
        run_batch(workspace)
    else:
        run_single(args.model, args.prompt, workspace)
