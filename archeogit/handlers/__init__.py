from . import blame


def get_handlers():
    handlers = {
        'blame': blame.handler,
    }
    return handlers
