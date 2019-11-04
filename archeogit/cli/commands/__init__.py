from . import blame


def get_commands():
    commands = [
        blame.BlameCommand(),
    ]
    return commands
