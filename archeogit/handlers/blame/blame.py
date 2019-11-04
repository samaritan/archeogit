import logging

from ... import utilities
from .formatters import CSVFormatter, PlaintextFormatter

logger = logging.getLogger(__name__)


def _get_suspects(sections):
    suspects = list()
    for section in sections:
        if not section.body['-']:  # No lines were deleted in this section
            suspects.extend(section.header)
            suspects.extend(section.footer)
        else:
            suspects.extend(section.body['-'])
    return sorted(list(set(suspects)))


class BlameHandler:
    def __init__(self, repository, commit, csv):
        self._repository = repository
        self._commit = commit
        self._csv = csv

    def handle(self):
        sections = self._repository.get_sections(self._commit)
        commits = dict()
        for path in sections:
            suspects = _get_suspects(sections[path])
            logger.debug(sections[path])
            logger.debug(suspects)
            commits[path] = self._repository.blamelines(
                self._commit, path, suspects
            )

        formatter = PlaintextFormatter()
        if self._csv:
            formatter = CSVFormatter()
        utilities.to_stdout(formatter.format(self._commit, commits))
