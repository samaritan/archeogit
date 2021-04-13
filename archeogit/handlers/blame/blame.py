import logging

from ... import blame, utilities, filters
from .formatters import CSVFormatter, PlaintextFormatter

logger = logging.getLogger(__name__)


class BlameHandler:
    def __init__(self, repository, commit, csv, enable_filters):
        self._repository = repository
        self._commit = commit
        self._csv = csv
        self._enable_filters = enable_filters

    def handle(self):
        commits = blame.blame(
            self._repository, self._commit, self.extract_filters())
        formatter = PlaintextFormatter()
        if self._csv:
            formatter = CSVFormatter()
        utilities.to_stdout(formatter.format(self._commit, commits))

    def extract_filters(self):
        filter_list = []
        for filter in self._enable_filters.split(','):
            if filter == "tests":
                filter_list.append(filters.TestsFilter())
        return filter_list
