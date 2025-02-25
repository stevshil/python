#!/bin/bash

if (( $# != 1 )); then
    echo "Usage: $0 <script.py>" 1>&2
    exit 1
fi

if ! -d virtual_env

python -m venv virtual_env

source virtual_env/bin/activate

pip install -r requirements.txt

python "$1"