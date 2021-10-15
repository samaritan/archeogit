import logging

from ... import blame, utilities
from .formatters import CSVFormatter, PlaintextFormatter

logger = logging.getLogger(__name__)


class BlameHandler:
    def __init__(self, repository, branch, commit, csv, filters):
        self._repository = repository
        self._branch = branch
        self._commit = commit
        self._csv = csv
        self._filters = filters

    def handle(self):
        commits = blame.blame(
            self._repository, self._branch, self._commit, self._filters)
        formatter = PlaintextFormatter()
        if self._csv:
            formatter = CSVFormatter()
        if commits:
            utilities.to_stdout(formatter.format(self._commit, commits))
