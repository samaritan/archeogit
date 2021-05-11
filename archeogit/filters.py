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
        source_file_extensions = ['java', 'c', 'h', 'cats', 'idc', 'cpp', 'c\+\+', 'cc', 'cp', 'cxx',
                                  'h\+\+', 'hh', 'hpp', 'hxx', 'inc', 'inl', 'ino', 'ipp', 're', 'tcc', 'tpp']
        extensions = '|'.join(source_file_extensions)
        return re.compile(fr'.*\.({extensions})$.*')


class DocumentationFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(docs?)\b')

    def __call__(self, path):
        return self._regex.search(path) is None
