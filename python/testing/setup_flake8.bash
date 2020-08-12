#!/bin/bash -ex

#Amazon Linux 2

# If a new virtual env was requested, then remove any old one.
if [ ${1:-'no'} == "new" ]
then
  if [ -d .venv ]
  then
    rm -rfv .venv
  fi
fi

# If there is no virtual env, then create one.
if [ ! -d .venv ]
then
  /usr/bin/env python3 -m venv .venv
fi

# Activate the virtual env.
. .venv/bin/activate

# pip install the tools
pip install flake8
pip list --format=columns
