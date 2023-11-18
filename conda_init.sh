#!/bin/bash

conda create --name codejam python==3.11 pip

eval "$(conda shell.bash hook)"

conda activate codejam

pip install numpy

pip install torch

pip install Django==4.2