# archeogit

`archeogit` is a Python utility to excavate a git repository in search of information.

The utility dentifies the change (commit, file, line) that last modified a line of code. Useful for identifying which change likely contributed to a vulnerability. Uses `git blame`.

## Installation

If you desire isolation of the environment onto which `archeogit`, and its dependencies are installed, setup and activate a virtual environment using `virtualenv --python=python3 .venv` and `. .venv/bin/activate`, respectively. Run `pip install -e .` or the included `./install.sh` to install `archeogit`.

## Configuration

The utility uses a configuration file to configure logging. The default configuration file---`config.json`---gets you started with all messages with a level of `INFO` or higher being logged to the console. Use the `--config-file` option on the command line to use a custom configuration file.

## Usage

The command line interface to the utility provides the ability to excavate different types of information from the git repository. The type of information to excavate is specified as a subcommand to the main interface.

### Main Interface

```
$ archeogit --help
usage: archeogit [-h] [--config-file CONFIG_FILE] {blame} ...

Command line utility to excavate a git repository.

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Path to the configuration file. Default is
                        config.json.

Supported Commands:
  {blame}
    blame               Blame commits likely to have contributed a bug.
```

### Command: `blame`

```
$ archeogit blame --help
usage: archeogit blame [-h] [--csv] repository commit

positional arguments:
  repository  Path to a git repository that has been cloned locally.
  commit      SHA-1 of the commit known to have fixed the bug.

optional arguments:
  -h, --help  show this help message and exit
  --csv       Generate output in CSV format. If unspecified, the output is
              plaintext formatted suitable for human consumption.
```

#### Example

```
$ archeogit blame ~/repositories/ffmpeg/ b97a4b658814b2de8b9f2a3bce491c002d34de31
libavcodec/cbs_av1.c

| Contributor                              | Frequency |
| ---------------------------------------- | --------- |
| c8c81ac5026c20ce60860dc9aa905e5e1634bed1 |        22 |
2019-11-04 14:27:18,626 - archeogit - blame excavation took 0.83 seconds
```

```
$ archeogit blame ~/repositories/ffmpeg/ b97a4b658814b2de8b9f2a3bce491c002d34de31 --csv
commit,path,contributor,frequency
b97a4b658814b2de8b9f2a3bce491c002d34de31,libavcodec/cbs_av1.c,c8c81ac5026c20ce60860dc9aa905e5e1634bed1,22
2019-11-04 14:27:22,798 - archeogit - blame excavation took 0.82 seconds
```

## Environment

The application has been tested on an environment identified below.

  * Ubuntu 18.04.3 LTS
  * Python 3.7.2
  * virtualenv 16.4.0
