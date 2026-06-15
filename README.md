# Agentic Malware Generation — LangGraph Multi-Agent System

An orchestrated multi-agent system for studying LLM-driven malware generation,
built with LangGraph. Extension of the v1 system (Generator + Reviewer + custom
Runner orchestrator) to a four-node typed state graph.

## Architecture

```
[START] → [Planner] → [Generator] → [Reviewer] → <route>
                           ↑                          |
                           |── "regenerate" ──────────┘
                           
                       "evasion" → [Evasion Analyst] → [END]
                       "end"     → [END]
```

### Agents

| Agent | Role | New in v2? |
|---|---|---|
| **Planner** | Decomposes raw prompt into structured `MalSpec` | ✅ New |
| **Generator** | Generates Python malware code from `MalSpec` | Evolved from v1 |
| **Reviewer** | Evaluates code against `MalSpec`, scores 0-10 | Evolved from v1 |
| **Evasion Analyst** | Analyzes final code for detectable patterns, produces hardened version | ✅ New |

### Key improvements over v1

1. **Typed state** — `MalGenState` TypedDict replaces freeform JSON inter-agent comms.
   The primary failure mode in v1 was JSON formatting errors in the reviewer loop
   (caused complete failure for Stable Code and Yi-Coder 9B). Pydantic schema
   validation in all structured queries eliminates this class of errors.

2. **Planner node** — Task decomposition is separated from code generation.
   In v1, raw prompts were sent directly to the Generator, leading to inconsistent
   interpretation across models. The Planner produces a structured `MalSpec` that
   all downstream agents evaluate against the same criteria.

3. **Evasion Analyst** — Post-convergence agent that evaluates final code for
   static AV signatures, behavioral EDR patterns, and string-based heuristics.
   Produces an evasion-hardened version of the approved code and an evasion score.

4. **LangGraph graph structure** — The custom while-loop in `runner.py` is replaced
   by a compiled `StateGraph` with explicit conditional edges. This gives full
   execution traces, checkpointing support, and clean separation of routing logic.

## Setup

```bash
pip install -r requirements.txt

# Start local LLM server (Ollama example)
ollama serve
ollama pull codegemma:7b
```

## Usage

```bash
# Single run
python runner.py --model codegemma:7b --prompt 1

# All models x all prompts (replicates original experiment)
python runner.py --batch
```

## Output structure

```
workspace/
  codegemma_7b_PROMPT1/
    codegemma_7b_P1_output.py        # final generated code
    codegemma_7b_P1_evasion.py       # evasion-hardened version
    final_output.json                # full run summary + trace
  batch_results.json                 # aggregate results across all runs
```

## Models tested

- CodeGemma 7B
- CodeQwen 7B  
- Codestral 22B
- StableCode 3B
- Yi-Coder 9B
- DeepSeek-Coder 6.7B
- CodeLlama 7B

## Ethical note

This system is designed for controlled cybersecurity research in isolated environments.
All testing uses network-isolated VMs. No external network calls are made during
code generation.
