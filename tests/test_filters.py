import pytest

from archeogit.filters import TestsFilter, NonSourceFilter, DocumentationFilter


def test_tests_filter():
    paths = ['/test/file', '/spec/file', '/tests/file', '/specs/file2']
    expected = {'/specs/file2'}

    tests_filter = TestsFilter()
    actual = set(filter(tests_filter.__call__, paths))

    assert actual == set(expected)


def test_nonsource_filter():
    paths = ['/src/program.java',
             '/src/program.c', '/docs/archeogit.py', 'CHANGES', '/src/program.pysomething']
    expected = {'/src/program.c', '/src/program.java'}

    nonsource_filter = NonSourceFilter()
    actual = set(filter(nonsource_filter.__call__, paths))

    assert actual == set(expected)


def test_documentation_filter():
    paths = ['docs/conf/httpd.conf.in', '/docs', '/doc/file', '/tests/file', 'CHANGES']
    expected = {'/tests/file', 'CHANGES'}

    documentation_filter = DocumentationFilter()
    actual = set(filter(documentation_filter.__call__, paths))

    assert actual == set(expected)
