import os


def read_file(file_name):
    if file_check(file_name):
        with open(file_name, "r") as file:
            result = file.read().split('\n')
        return result
    return None


def read_cli(params):
    return " ".join(params).split(", ")


def file_check(file_name):
    if os.path.isfile(file_name) and file_name.endswith(".txt"):
        return True
    return False
