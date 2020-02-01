import json


def decode_bytes_to_dict(data):
    return json.loads(data.decode("utf-8").replace("'", '"'))