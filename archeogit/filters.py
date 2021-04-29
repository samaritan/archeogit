from . import utilities
import re


def get_filters():
    filters = {"test": TestsFilter(), "docs": DocumentationFilter(),
               "nonsource": NonSourceFilter()}
    return filters


class Filter():
    def __call__(self, path):
        pass


class TestsFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(tests?|spec)\b')

    def __call__(self, path):
        return not bool(self._regex.search(path))


class NonSourceFilter(Filter):
    def __call__(self, path):
        pass


class DocumentationFilter(Filter):
    def __call__(self, path):
        return "docs" not in path.split("/")
