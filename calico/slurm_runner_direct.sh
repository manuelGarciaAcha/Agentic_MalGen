#!/bin/bash
#SBATCH --job-name=slurm_runner_direct
#SBATCH --output=logs/slurm_runner_direct.log
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gres=gpu:a100-40G

export OLLAMA=$HOME/bin/ollama
export OLLAMA_MODELS=$HOME/ollama-models/

$OLLAMA serve > ollama-server_direct.log 2>&1 &
sleep 10


cd $HOME/agent/

MODELS=$($OLLAMA list | awk 'NR>1 {print $1}')

echo "PROMPTS: $PROMPT_IDS"
echo "MODELS: $MODELS"

echo "========================================"
echo "RUNNING FULL BATCH"
echo "========================================"

python direct_runner.py --batch 

echo "ALL RUNS FINISHED"
