#!/bin/bash

if [[ -d .venv ]]; then
  source .venv/bin/activate
else
  virtualenv .venv
  source .venv/bin/activate
fi

pip install -r requirements.txt
