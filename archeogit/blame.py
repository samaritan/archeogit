import logging

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


def blame(repository, branch, commit, filters=None):
    commits = dict()
    if branch not in set(repository.branches.with_commit(commit)):
        logger.warn(
            '`%s` is not in default branch of `%s`. Exiting.', commit.id,
            repository.workdir
        )
        return commits

    sections = repository.get_sections(commit)
    paths = list(sections.keys())
    if filters is not None:
        for filter_class in filters:
            paths = filter(filter_class.__call__, paths)

    for path in paths:
        suspects = _get_suspects(sections[path])
        commits[path] = repository.blamelines(commit, path, suspects)
    return commits
