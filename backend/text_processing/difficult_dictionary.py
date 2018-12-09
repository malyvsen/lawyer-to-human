import json

def read_dict(self, path):
    with open(path, 'r') as f:
        return json.load(f)