def standerdize(path):
    path_list = path.split("/")
    stack = []
    for p in path_list:
        if p == ".":
            continue
        elif p == "..":
            stack.pop()
        else:
            stack.append(p)
    return "/".join(stack)


print(standerdize("/usr/bin/../bin/./scripts/../")) # "/usr/bin/"
