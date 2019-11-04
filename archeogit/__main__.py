import logging
import time

from logging.config import dictConfig

from . import utilities
from .cli import CLI, commands
from .handlers import get_handlers


def _configure_logging(configuration):
    dictConfig(configuration['logging'])


def main():
    cli = CLI(commands.get_commands(), get_handlers())
    arguments = cli.get_arguments()

    configuration = utilities.JSON.read(arguments.config_file)
    _configure_logging(configuration)
    logger = logging.getLogger('archeogit')

    start = time.time()
    arguments.handler(arguments)
    elapsed = time.time() - start
    logger.info('%s excavation took %.2f seconds', arguments.command, elapsed)


if __name__ == '__main__':
    main()
