#!/usr/bin/env python3

import argparse
import boto3
import base64
import json
import logging
from botocore.exceptions import ClientError


# function to get secret
def get_secret(secret_name, region_name):

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the
            # provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current
            # state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        else:
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these
        # fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(
              get_secret_value_response['SecretBinary'])
            return decoded_binary_secret
    # Function ends here.


# main
def main():
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='get_aws_secret',
                                        description='Get a secret from AWS'
                                        + 'Secrets Manager.',
                                        fromfile_prefix_chars='@',
                                        epilog='... "from file" with prefix @'
                                        )

    # Add the arguments
    my_parser.add_argument('Secret Name',
                           metavar='name',
                           type=str,
                           help='the name of the secret')

    my_parser.add_argument('AWS Region',
                           metavar='region',
                           type=str,
                           help='the AWS region where the secret is stored',
                           choices=['us-east-1', 'us-east-2', 'us-west-1',
                                    'us-west-2', 'af-south-1', 'ap-east-1',
                                    'ap-south-1', 'ap-northeast-2',
                                    'ap-southeast-1', 'ap-southeast-2',
                                    'ap-northeast-1', 'ca-central-1',
                                    'eu-central-1', 'eu-west-1', 'eu-west-2',
                                    'eu-south-1', 'eu-west-3', 'eu-north-1',
                                    'me-south-1', 'sa-east-1'])

    # Execute the parse_args() method
    args = my_parser.parse_args()
    args_as_vars = vars(args)
    region_name = args_as_vars['AWS Region']
    secret_name = args_as_vars['Secret Name']

    # Run the function to get the secret
    result = json.loads(get_secret(secret_name, region_name))
    result_key = list(result.keys())[0]
    result_value = result[result_key]

    # print out the secret!
    print(result_value)

    # Bibliography
    # https://realpython.com/command-line-interfaces-python-argparse/


if __name__ == '__main__':  # noqa: F821
    logging.basicConfig()
    main()
