import logging

from ... import blame, utilities
from ...filters import get_filters
from .formatters import CSVFormatter, PlaintextFormatter

logger = logging.getLogger(__name__)


class BlameHandler:
    def __init__(self, repository, commit, csv, filters):
        self._repository = repository
        self._commit = commit
        self._csv = csv
        self._filters = filters

    def handle(self):
        commits = blame.blame(
            self._repository, self._commit, self.extract_filters())
        formatter = PlaintextFormatter()
        if self._csv:
            formatter = CSVFormatter()
        utilities.to_stdout(formatter.format(self._commit, commits))

    def extract_filters(self):
        filter_list = []
        filters = get_filters()
        print(filters)
        if self._filters:
            for a_filter in self._filters.split(','):
                filter_list.append(filters[a_filter])
        print(filter_list)
        return filter_list
