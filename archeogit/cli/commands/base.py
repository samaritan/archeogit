class BaseCommand:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def add_subparser(self, parsers, handler):
        parser = parsers.add_parser(self._name, help=self._description)
        parser.set_defaults(handler=handler)
        return parser

    @property
    def name(self):
        return self._name
