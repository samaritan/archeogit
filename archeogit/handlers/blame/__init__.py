import argparse
import os
import re

from .blame import BlameHandler
from ...repository import Repository

_SHA1_RE = re.compile(r'\b[0-9a-f]{,40}\b')


def _validate(arguments):
    _validate_repository(arguments.repository)
    _validate_commit(arguments.commit)


def _validate_repository(repository):
    if not os.path.exists(repository):
        msg = f'{repository} does not exist.'
        raise argparse.ArgumentException(None, msg)
    if not os.path.exists(os.path.join(repository, '.git')):
        msg = f'{repository} not a valid git repository.'
        raise argparse.ArgumentException(None, msg)


def _validate_commit(commit):
    if not _SHA1_RE.match(commit):
        msg = f'{commit} is not a valid SHA-1'
        raise argparse.ArgumentException(None, msg)


def handler(arguments):
    _validate(arguments)

    repository = Repository(arguments.repository)
    commit = repository.get(arguments.commit)
    _handler = BlameHandler(repository, commit, arguments.csv)
    _handler.handle()
