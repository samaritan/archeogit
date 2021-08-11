from ... import filters
from .base import BaseCommand


class BlameCommand(BaseCommand):
    def __init__(self):
        name = 'blame'
        description = 'Blame commits likely to have contributed a bug.'
        super().__init__(name, description)

    def add_subparser(self, parsers, handler):
        parser = super().add_subparser(parsers, handler)
        parser.add_argument(
            'repository', help='Path to a git repository that has been cloned '
            'locally.'
        )
        parser.add_argument(
            'branch', help='Name of the default branch of the repository.'
        )
        parser.add_argument(
            'commit', help='SHA-1 of the commit known to have fixed the bug.'
        )
        parser.add_argument(
            '--csv', action='store_true', help='Generate output in CSV '
            'format. If unspecified, the output is plaintext formatted '
            'suitable for human consumption.'
        )
        parser.add_argument(
            '--filters', nargs='*', choices=filters.FILTERS.keys(),
            help='Add filters to prevent certain files from being blamed.'
        )
