config = {"ExcludeTestFileName": True, "ExcludeTestDirectory": True}

def exclude(path):
    return excludeTestDirectory(path) or excludeTestFileName(path)

def excludeTestFileName(path):
    if config["ExcludeTestFileName"]:
        return "Test" in path
    else:
        return False

def excludeTestDirectory(path):
    if config["ExcludeTestDirectory"]:
        return "test" in path.split("/")
    else:
        return False