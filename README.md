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
   ``` 
       sudo systemctl edit ollama
       # within ollama config:
       OLLAMA_DEBUG=1
       OLLAMA_FLASH_ATTENTION=1```
2. Enter venv
   ``` source ./<venv_dir>/bin/activate```
3. install dependencies (OpenAI only for now)

### Framework:
Currently observed functionality:
  > Generate Code
> Review Code
> Output Code and Review into files
