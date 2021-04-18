class Filter():
    def __call__(self, path):
        pass


class TestsFilter(Filter):
    def __call__(self, path):
        return not ("Test" in path or "test" in path.split("/"))


class NonSourceFilter(Filter):
    def __call__(self, path):
        pass


class DocumentationFilter(Filter):
    def __call__(self, path):
        return "docs" not in path.split("/")
