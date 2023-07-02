#!/bin/bash
source ~/anaconda3/etc/profile.d/conda.sh
cd "$1"
conda activate nlp_tools
python "$2.py" "$3"
