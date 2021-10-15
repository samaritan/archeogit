from setuptools import setup

VERSION = None
with open("VERSION", "r") as file_:
    VERSION, _ = file_.read().split('-')

setup(
    name='archeogit',
    version=VERSION,
    packages=['archeogit'],
    install_requires=['jinja2~=2.10', 'pygit2~=0.28'],
    entry_points={
        'console_scripts': [
            'archeogit = archeogit.__main__:main'
        ]
    }
)
