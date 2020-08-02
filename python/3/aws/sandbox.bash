#!/bin/bash 
#Amazon Linux 2.

# Install python3
which python3
if [ $? -ne 0 ]
then
  yum install -y python3
fi

# Remove the old virtual environment.
if [ -d ./venv ]
then
  rm -fvr ./venv
fi

# Make a new virtual environment.
python3 -m venv venv
. ./venv/bin/activate

# Install awscommon which includes botocore and boto3.
pip install wheel
pip install awscommons
pip install urllib3[secure]

# List out what is installed.
pip list --format=columns


