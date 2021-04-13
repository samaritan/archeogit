class Filter():
    def __init__(self):
        pass

    def do_filter(self, path):
        pass


class TestsFilter(Filter):
    def __init__(self):
        pass

    def do_filter(self, path):
        if "Test" in path or "test" in path.split("/"):
            return False
        else:
            return True
