import argparse
import os
import re

from .blame import BlameHandler
from ...filters import get_filters
from ...repository import Repository

_SHA1_RE = re.compile(r'^[0-9a-f]{7,40}$')


def validate(arguments):
    _validate_repository(arguments.repository)
    _validate_commit(arguments.commit)


def _validate_repository(repository):
    if not os.path.exists(repository):
        msg = f'{repository} does not exist.'
        raise argparse.ArgumentError(None, msg)
    if not os.path.exists(os.path.join(repository, '.git')):
        msg = f'{repository} not a valid git repository.'
        raise argparse.ArgumentError(None, msg)


def _validate_commit(commit):
    if not _SHA1_RE.match(commit):
        msg = f'{commit} is not a valid SHA-1'
        raise argparse.ArgumentError(None, msg)


def handler(arguments):
    validate(arguments)

    repository = Repository(arguments.repository)
    commit = repository.get(arguments.commit)
    if commit is None:
        msg = f'{arguments.commit} is not a valid SHA-1 in '                  \
              f'{arguments.repository}'
        raise Exception(msg)
    filters = list()
    if arguments.filters is not None:
        filters = get_filters()
        filters = [filters[f] for f in arguments.filters]
    _handler = BlameHandler(
        repository, commit, arguments.csv, filters)
    _handler.handle()
