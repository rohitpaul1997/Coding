def simplifyPath(path: str) -> str:
    directories, stack = path.split("/"), []

    for directory in directories:
        if directory == "" or directory == ".":
            continue
        elif directory == ".." and stack:
            stack.pop()
        elif directory == "..":
            continue
        else:
            stack.append(directory)

    return "/" + "/".join(stack)
