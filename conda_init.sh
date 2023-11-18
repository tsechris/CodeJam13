#!/bin/bash

if conda info --envs | grep -q codejam; then echo "base already exists"; else conda create --name codejam python==3.11 pip; fi

eval "$(conda shell.bash hook)"

conda activate codejam

pip install numpy

pip install torch

pip install Django==4.2