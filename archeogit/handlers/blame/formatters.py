import collections

from jinja2 import Environment, FileSystemLoader


def _flatten(excavation):
    flattened = dict()
    for (path, excavations) in excavation.items():
        distribution = collections.Counter(excavations)
        flattened[path] = sorted(
            distribution.items(), key=lambda i: i[1], reverse=True
        )
    return flattened


class Formatter:
    def __init__(self, template):
        loader = FileSystemLoader('archeogit/handlers/blame/templates')
        environment = Environment(loader=loader)
        self._template = environment.get_template(template)

    def format(self, commit, excavation):
        excavation = _flatten(excavation)
        return self._template.render(commit=commit, excavation=excavation)


class CSVFormatter(Formatter):
    def __init__(self):
        super().__init__('csv')


class PlaintextFormatter(Formatter):
    def __init__(self):
        super().__init__('plaintext')
