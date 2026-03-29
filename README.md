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

##### Generator (FUNCTIONAL):

Recieved input: 
 - 1st Iteration: Runner.py call
 - 2nd Iteration - Max_Iteration: Review_Result() from the Reviewer.
 
 Generated Output (to Reviewer):
 - Draft(), defined in core/comms.py

##### Reviewer (UNDER-DEV):

 Recieved input: 
 - Draft() from the Generator
 
 Generated Output (to Generator and Runner):
 - Review_Result(), defined in core/comms.py

##### Runner (ON-HOLD):
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

### NOTE:

Need to cite: ollama, models used, etc

