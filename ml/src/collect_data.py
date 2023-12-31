import argparse
import yaml
from io import StringIO


parser = argparse.ArgumentParser()
parser.add_argument('--chunk', help='chunk of data')
parser.add_argument('--params', help='path to params.yaml')
args = parser.parse_args()


def main():
    params = load_params(args.params)
    collect_data(params['base']['data_dir'], args.chunk)


def collect_data(data_dir: str, chunk: str):
    with open(f'{data_dir}/raw/data.csv', 'a') as f:
        for _ in range(ord(chunk[0])):
            f.write(generate_line() + '\n')


def generate_line() -> str:
    return f'{generate_random_string(10)},{generate_random_string(10)},{generate_random_string(10)},{generate_random_string(10)}'

def generate_random_string(length):
    result = StringIO()
    with open('/dev/random', 'rb') as f:
        while result.tell() < length:
            random_bytes = f.read(1)
            char = chr(random_bytes[0])
            if char.isalpha():
                result.write(char)
    return result.getvalue()


def load_params(filename: str):
    with open(filename, 'r') as f:
        params = yaml.safe_load(f)
        return params 

if __name__ == '__main__':
    main()
