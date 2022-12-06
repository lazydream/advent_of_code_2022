import os


__all__ = ['get_path', 'get_input']


def get_path(file):
    return os.path.dirname(os.path.abspath(file)) + '\input.txt'


def get_input(link: str):
    with open(link) as f:
        for line in f:
            yield line.strip()
