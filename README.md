# Agentic Malware Generation — LangGraph Multi-Agent System

An orchestrated multi-agent system for studying LLM-driven malware generation,
built with LangGraph. Extension of the v1 system (Generator + Reviewer + custom
Runner orchestrator) to a four-node typed state graph.

## Context

This implementation is used in the study "Evaluating Agentic AI Frameworks for Malware Generation."

## Architecture

```
[START] → [Planner] → [Generator] → [Reviewer] → <route>
                           ↑                          |
                           |── "regenerate" ──────────┘
                           
                       "evasion" → [Evasion Analyst] → [END]
                       "end"     → [END]
```

### Agents

| Agent | Role |
|---|---|
| **Planner** | Decomposes raw prompt into structured `MalSpec` |
| **Generator** | Generates Python implementation from `MalSpec` |
| **Reviewer** | Evaluates code against `MalSpec`, scores 0-10 |
| **Evasion Analyst** | Analyzes final code for detectable patterns, produces hardened version |

## Repository Structure

agents/              Agent implementations
core/                Shared interfaces: prompts, model, state
calico/              Cluster ulitities
workspace*/          Generated outputs
graph.py             LangGraph definiton
runner.py            Agentic orchestration script
direct_runner.py     Single Pass orchestration script

## Setup (Local)

```bash
pip install -r requirements.txt

# Start local LLM server (Ollama example)
ollama serve
ollama pull codegemma:7b
```

## Experimental Configuration

Models: 10
Prompts: 4
Conditions:
- Agentic/Iterative
- Single Pass

Trails per Condition: 2

Total Executions: 160

## Usage (Local)

```bash
# Agentic Condition
python runner.py --batch

# Single Pass Condition
python direct_runner.py --batch
```

## Setup (Calico Cluster)

```bash
pip install -r requirements.txt

# Pull models from Ollama
cd calico
sbatch ollama_model_load.sh
```

## Usage (Calico Cluster)
``` bash 
cd calico

# Run agentic framework
sbatch slurm_runner.sh

# Run single-pass
sbatch slurm_runner_direct.sh
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

- yi-coder:9b 
- codeqwen:7b 
- qwen2.5-coder:32b
- vanilj/trinity-2-codestral-22b-v0.2:4_k_m 
- codegemma:7b 
- phind-codellama:34b 
- codestral:22b 
- stable-code:3b 
- deepseek-coder:6.7b 
- codellama:7b 

## Ethical note

This system is designed for controlled cybersecurity research in isolated environments.
All testing uses network-isolated VMs. No external network calls are made during
code generation.
