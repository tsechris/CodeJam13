#!/bin/bash

if conda info --envs | grep -q codejam; then echo "codejam already exists"; else conda create --name codejam python==3.11 pip; fi

eval "$(conda shell.bash hook)"

conda activate codejam

conda install cudatoolkit

pip3 install torch torchvision torchaudio

pip install numpy

pip install Django==4.2

pip install kaleido

pip install requests

pip install plotpy

pip install plotvision

pip install pathlib

pip install opendatasets