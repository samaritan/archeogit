import argparse
import tempfile

import pytest

from archeogit import cli


def _get_arguments(config_file):
    return argparse.Namespace(config_file=config_file)


def test_validate_raises_argumenterror_config_file():
    pattern = 'Configuration file .* not found.'
    with pytest.raises(argparse.ArgumentError, match=pattern):
        arguments = _get_arguments('/path/to/no/configuration.json')
        cli.validate(arguments)


def test_validate():
    with tempfile.NamedTemporaryFile() as config_file:
        arguments = _get_arguments(config_file.name)
        assert cli.validate(arguments) is None
