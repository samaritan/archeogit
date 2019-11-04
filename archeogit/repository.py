import pygit2

from .models import Hunk, Line, Section


def _get_diff(commit, parent=None):
    if parent is not None:
        return commit.tree.diff_to_tree(parent.tree, swap=True)
    return commit.tree.diff_to_tree(swap=True)


def _get_hunks(commit):
    hunks = dict()

    parent = commit.parents[0] if commit.parents else None
    for patch in _get_diff(commit, parent):
        path = patch.delta.new_file.path
        hunks[path] = list()
        for hunk in patch.hunks:
            hunks[path].append(Hunk(lines=_get_lines(hunk)))

    return hunks


def _get_lines(hunk):
    lines = list()

    for line in hunk.lines:
        origin = line.origin
        lineno = line.new_lineno if origin == '+' else line.old_lineno
        lines.append(Line(lineno, origin))

    return lines


def _get_sections(hunks):
    sections = dict()

    for path in hunks:
        sections[path] = list()
        for hunk in hunks[path]:
            sections[path].extend(_get_sectionsforlines(hunk.lines))

    return sections


def _get_sectionsforlines(lines):
    sections = list()

    index = 0
    header, footer = list(), list()
    while index < len(lines):
        # Section Header
        if not header:
            while lines[index].change == ' ':
                header.append(lines[index].number)
                index += 1

        # Section Body
        body = {'+': list(), '-': list()}
        while index < len(lines) and lines[index].change != ' ':
            body[lines[index].change].append(lines[index].number)
            index += 1

        # Section Footer
        while index < len(lines) and lines[index].change == ' ':
            footer.append(lines[index].number)
            index += 1

        sections.append(Section(header, body, footer))

        header = footer
        footer = list()

    return sections


class Repository(pygit2.Repository):
    def get_sections(self, commit):
        return _get_sections(_get_hunks(commit))

    def blamelines(self, commit, path, lines):
        modifiers = list()

        if commit.parents:
            parent = commit.parents[0]
            blame = self.blame(path, newest_commit=parent.id)
        else:
            blame = self.blame(path)

        for line in lines:
            hunk = blame.for_line(line)
            modifiers.append(hunk.orig_commit_id)

        return modifiers
