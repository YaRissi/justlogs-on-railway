import os
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)


def load_json_file(file_path: str) -> dict:
    """Loads a json file

    Args:
        file_path (str): path to the json file

    Returns:
        dict: the json file as a dictionary
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json_file(file_path: str, data: dict) -> None:
    """Writes a dictionary to a json file
    
    Args:
        file_path (str): path to the json file
        data (dict): data to write to the file
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def convert_args(data: dict) -> dict:
    """Converts the arguments from the environment variables to the data dictionary

    Args:
        data (dict): data template

    Returns:
        dict: data with injected environment variables
    """
    data['admins'] = os.getenv('ADMINS', '').split(',')
    data['adminAPIKey'] = os.getenv('ADMINAPIKEY', '')
    data['username'] = os.getenv('USERNAME', '')
    data['oauth'] = os.getenv('OAUTHTOKENFORCHAT', '')
    data['clientID'] = os.getenv('MYTWITCHCLIENTID', '')
    data['clientSecret'] = os.getenv('MYSECRETCLIENTID', '')
    data['botVerified'] = os.getenv('BOTVERIFIED', '').lower() == 'true'
    data['logLevel'] = os.getenv('LOGLEVEL', '')
    data['channels'] = os.getenv('CHANNELS', '').split(',')
    return data

if __name__ == '__main__':
    args = parser.parse_args()
    input = load_json_file(args.input)
    converted_file = convert_args(input)
    write_json_file(args.output, converted_file)