sandbox.bash
------------

A quick way to setup a virtual environment for Python 3 with botocore, boto3 and urllib3 installed.

get_aws_secret.py
-----------------

A command line tool for automation that gets a secret from AWS Secrets Manager.
- Can be used with a config file, or take command line arguments, or both. e.g.:
<pre><code># ./get_aws_secret.py @args.txt eu-west-2
prints_out_some_secret_here...
</code></pre>

