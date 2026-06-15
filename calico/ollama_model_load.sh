#!/bin/bash
#SBATCH --job-name=ollama_model_load
#SBATCH --output=logs/ollama_model_load.log
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

export OLLAMA_MODELS=$HOME/ollama-models
export OLLAMA=$HOME/bin/ollama
mkdir -p "$OLLAMA_MODELS"

$OLLAMA serve > ollama-server.log 2>&1 &
sleep 10

$OLLAMA pull phind-codellama:34b
$OLLAMA pull vanilj/trinity-2-codestral-22b-v0.2:4_k_m
$OLLAMA pull qwen2.5-coder:32b
$OLLAMA pull codegemma:7b
$OLLAMA pull yi-coder:9b
$OLLAMA pull codeqwen:7b
$OLLAMA pull codellama:7b
$OLLAMA pull deepseek-coder:6.7b
$OLLAMA pull stable-code:3b
$OLLAMA pull codestral:22b

echo "Complete"