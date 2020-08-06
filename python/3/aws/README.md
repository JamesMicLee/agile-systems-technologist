[sandbox.bash](sandbox.bash)
------------

A quick way to setup a virtual environment for Python 3 with botocore, boto3 and urllib3 installed.

[test_py.bash](test_py.bash)
------------
A bash script for testing Python code with Flake8. e.g.:
<pre><code># ./test_py.bash sample_code.py
sample_code.py:3:80: E501 line too long (104 > 79 characters)
sample_code.py:3:105: W291 trailing whitespace
</code></pre>

[get_aws_secret.py](./secrets_manager/get_aws_secret.py)
-----------------

A command line tool for automation that gets a secret from AWS Secrets Manager.
- Can be used with a config file, or take command line arguments, or both. e.g.:
<pre><code># ./get_aws_secret.py @args.txt eu-west-2
prints_out_some_secret_here...
</code></pre>

