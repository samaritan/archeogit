from setuptools import setup

setup(
    name='archeogit',
    version='0.2.0',
    packages=['archeogit'],
    install_requires=['jinja2~=2.10', 'pygit2~=0.28'],
    entry_points={
        'console_scripts': [
            'archeogit = archeogit.__main__:main'
        ]
    }
)
