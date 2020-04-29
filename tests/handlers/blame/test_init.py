import argparse
import os
import tempfile

import pytest

from archeogit.handlers import blame


def _get_arguments(repository, commit):
    return argparse.Namespace(repository=repository, commit=commit)


TESTDATA = [
    ('/invalid/path/to/repository', '.* does not exist.'),
    (tempfile.gettempdir(), '.* not a valid git repository.'),
]
@pytest.mark.parametrize('repository,pattern', TESTDATA)
def test_validate_raises_argumenterror_repository(repository, pattern):
    with pytest.raises(argparse.ArgumentError, match=pattern):
        arguments = _get_arguments(repository, 'eff9507')
        blame.validate(arguments)


def test_validate():
    arguments = _get_arguments(os.getcwd(), 'eff9507')
    assert blame.validate(arguments) is None
