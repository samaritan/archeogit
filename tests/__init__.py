import os
import pytest

DATA_ROOT = os.path.join(os.path.dirname(__file__), 'data')
_REASON = 'Test repository not found. Use `git submodule` to clone.'


def requirerepositoryformodule(name):
    if not os.path.exists(os.path.join(DATA_ROOT, name, '.git')):
        pytest.skip(_REASON, allow_module_level=True)
