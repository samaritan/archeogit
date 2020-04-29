import argparse
import os


def validate(arguments):
    _validate_configfile(arguments.config_file)


def _validate_configfile(config_file):
    if not os.path.exists(config_file):
        msg = f'Configuration file {config_file} not found.'
        raise argparse.ArgumentError(None, msg)


class CLI:
    def __init__(self, commands, handlers):
        self._parser = argparse.ArgumentParser(
            description='Command line utility to excavate a git repository.'
        )
        self._parser.add_argument(
            '--config-file', default='configuration.json', help='Path to '
            'the configuration file. Default is configuration.json.'
        )
        subparsers = self._parser.add_subparsers(title='Supported Commands')
        subparsers.required = True
        subparsers.dest = 'command'
        self._attach_subparsers(subparsers, commands, handlers)

    def get_arguments(self):
        arguments = self._parser.parse_args()
        validate(arguments)
        return arguments

    def _attach_subparsers(self, subparsers, commands, handlers):
        for command in commands:
            handler = handlers.get(command.name, None)
            if handler is not None:
                command.add_subparser(subparsers, handler)
