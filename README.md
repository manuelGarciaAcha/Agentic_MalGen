# Agentic_MalGen

Shared Repository for Agentic Malware Generation Research

### Prequisites:

- Ollama
- python3
- pip
- sudo privileges
- code capable model installed locally (Current code targeting Stable-Code(4b quantized))
- OpenAI python library
  
``` SUGGESTION: Create a python venv to work within ```

### Agent Setup (Debian):

1. Edit ollama configs for increased performance:
   ``` sudo systemctl edit ollama
       # within ollama config:
       OLLAMA_DEBUG=1
       OLLAMA_FLASH_ATTENTION=1```
2. Enter venv
   ``` source ./<venv_dir>/bin/activate```
3. install dependencies (OpenAI only for now)

### Framework:

2-agent framework that implements a generation agent and a review agent.
- Both agents are managed by a parent script (runner.py) where framework goal is defined.
- Agents are constrained to only output JSON in order to have clean and predictable parsing while looping.

##### Generator:

Recieved input: 
 - 1st Iteration: Runner.py call
 - 2nd Iteration - Max_Iteration: Review_Result() from the Reviewer.
 
 Generated Output (to Reviewer):
 - Draft(), defined in core/comms.py

##### Reviewer:

 Recieved input: 
 - Draft() from the Generator
 
 Generated Output (to Generator and Runner):
 - Review_Result(), defined in core/comms.py

##### Runner:
 - Manages Agent communications.
 - Compares Agent outputs to predefined metrics (TBD)
 - Initializes and Ends Agentic Loop.


### Usage:

- Prompt, scoring criteria/metrics and workspace directory are modified, per run via CLI execution of the runner.

``` 
   cd agent
   source ./.venv/bin/activate
   python3 runner.py <prompt_number> <model_name>
   
```

### Script Breakdown and Summaries:
  - runner.py: the main orchestrator program, which includes the agentic control loop, logging, JSON to Python conversion, and execution

agents/
  - generator.py: generator agent setup. Includes model prompt to create the "context" for the agent. Preparation of Draft output also included here.
  - reviewer.py: reviewer agent setup. Similar to generator, but with different context and also includes code review criteria

core/
  - comms.py: includes dataclass defenitions, specifically for communication configurations between agents and orchestrator
  - model.py: creates the interface between agents and LLM
  - prompts.py: simple dictionary with all 4 prompts

logs/
  - slurm_runner.log: calico output, included for debugging

workspace and workspace2: where all outputs are iteration logs are written to.

### NOTE:

Need to cite: ollama, models used, etc

