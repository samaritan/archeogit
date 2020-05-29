import io
import json
import logging
import platform
import subprocess
import sys
import threading

logger = logging.getLogger(__name__)


class JSON:
    @staticmethod
    def read(path):
        with open(path) as file:
            return json.load(file)


def run(command, directory):
    def _exit(process, stream):
        process.wait()
        logger.debug('%s returned %d', process.args, process.returncode)

        error = stream.read()
        if error != '':
            logger.error(error)

    process = subprocess.Popen(
        command, cwd=directory, shell=not platform.system() == 'Windows',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    ostream = io.TextIOWrapper(process.stdout, errors='replace')
    estream = io.TextIOWrapper(process.stderr, errors='replace')

    thread = threading.Thread(target=_exit, args=(process, estream,))
    thread.start()

    return ostream, thread


def to_stderr(text):
    sys.stderr.write('{}\n'.format(text))


def to_stdout(text):
    sys.stdout.write('{}\n'.format(text))
