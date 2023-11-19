#!/bin/bash

eval "$(conda shell.bash hook)"

conda activate codejam

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "${SCRIPT_DIR}"/EcoSnap

python manage.py runserver 0.0.0.0:8080