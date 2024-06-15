import os
import argparse
import json
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)


def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def split_env_var(env_var):
    """Helper function to split an environment variable by comma."""
    return env_var.split(",") if env_var and "," in env_var else [env_var]

def convert_args(data):
    data['admins'] = split_env_var(os.getenv('ADMINS', ''))
    data['adminAPIKey'] = os.getenv('ADMINAPIKEY', '')
    data['username'] = os.getenv('USERNAME', '')
    data['oauth'] = os.getenv('OAUTHTOKENFORCHAT', '')
    data['clientID'] = os.getenv('MYTWITCHCLIENTID', '')
    data['clientSecret'] = os.getenv('MYSECRETCLIENTID', '')
    data['botVerified'] = os.getenv('BOTVERIFIED', '').lower() == 'true'
    data['logLevel'] = os.getenv('LOGLEVEL', '')
    data['channels'] = split_env_var(os.getenv('CHANNELS', ''))
    return data

if __name__ == '__main__':
    args = parser.parse_args()
    input = load_json_file(args.input)
    converted_file = convert_args(input)
    write_json_file(args.output, converted_file)