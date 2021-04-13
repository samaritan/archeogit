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


def blame(repository, commit, filters):
    commits = dict()
    sections = repository.get_sections(commit)
    paths = list(sections.keys())
    for filter_object in filters:
        paths = filter(filter_object.do_filter, paths)

    for path in paths:
        suspects = _get_suspects(sections[path])
        commits[path] = repository.blamelines(commit, path, suspects)
    return commits
