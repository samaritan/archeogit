import json
import sys


class JSON:
    @staticmethod
    def read(path):
        with open(path) as file:
            return json.load(file)


def to_stderr(text):
    sys.stderr.write('{}\n'.format(text))


def to_stdout(text):
    sys.stdout.write('{}\n'.format(text))
