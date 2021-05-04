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
    def __init__(self):
        self._regex = self.create_regex()

    def __call__(self, path):
        return bool(self._regex.search(path))

    def create_regex(self):
        source_file_extensions = ["java", "c", "h"]

        non_source_regex_segment = r''
        for extension in source_file_extensions:
            non_source_regex_segment += (extension + '|')
        non_source_regex_segment = non_source_regex_segment[0:-1]
        # Expression looks for nonsource files in list and paths without extension
        return re.compile(r'^.*\.(' + non_source_regex_segment + r')')


class DocumentationFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(docs?)\b')

    def __call__(self, path):
        return not bool(self._regex.search(path))
