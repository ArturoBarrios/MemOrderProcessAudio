#!/bin/bash

set -e

if [ ! -d "venv" ]; then
  python3.11 -m venv venv
fi

source venv/bin/activate
python --version
which python
pip install --upgrade pip
pip install -r requirements.txt

python run_audio_pipeline.py
