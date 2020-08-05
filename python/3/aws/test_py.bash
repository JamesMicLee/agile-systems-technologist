#!/bin/bash 
#Amazon Linux 2.

# Install python3
which python3 >/dev/null
if [ $? -ne 0 ]
then
  yum install -y python3
fi

# Remove the old virtual environment.
if [ -d ./.py_test_venv ]
then
  rm -fr ./.py_test_venv
fi

# Make a new virtual environment.
python3 -m venv .py_test_venv
. .py_test_venv/bin/activate

# Install awscommon which includes botocore and boto3.
pip -q install flake8 

# List out what is installed.
# pip list --format=columns

flake8 ${1:-*.py}
