import json
import os
import pickle


def mkdir(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)


def json_load(path):
    with open(path, 'r') as file:
        json_file = json.load(file)
    return json_file


def json_write(path, label):
    with open(path, 'w') as file:
        json.dump(label, file)


def pickle_load(path):
    with open(path, 'rb') as file:
        f = pickle.load(file)
    return f


def pickle_write(path, label):
    with open(path, 'wb') as file:
        pickle.dump(label, file)
