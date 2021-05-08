from . import utilities
import re


def get_filters():
    filters = {'test': TestsFilter(), 'docs': DocumentationFilter(),
               'nonsource': NonSourceFilter()}
    return filters


class Filter():
    def __call__(self, path):
        pass


class TestsFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(tests?|spec)\b')

    def __call__(self, path):
        return self._regex.search(path) is None


class NonSourceFilter(Filter):
    def __init__(self):
        self._regex = self.create_regex()

    def __call__(self, path):
        return self._regex.search(path) is not None

    def create_regex(self):
        source_file_extensions = ['java', 'c', 'h']
        return re.compile(fr"^.*\.({'|'.join(source_file_extensions)})")


class DocumentationFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(docs?)\b')

    def __call__(self, path):
        return self._regex.search(path) is None
