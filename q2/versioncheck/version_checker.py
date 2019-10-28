def comparator(v1, v2):
    v1_array, v2_array = v1.split("."), v2.split(".")
    for x, y in zip(v1_array, v2_array):
        if int(x) > int(y):
            return 1
        elif int(x) < int(y):
            return -1

    if len(v1_array) > len(v2_array):
        return 1
    elif len(v1_array) < len(v2_array):
        return -1
    return 0


def version_checker(version1, version2):
    mapper = {
        0: "equal to",
        1: "greater than",
        -1: "less than"
    }
    res = comparator(version1, version2)
    return "%s is %s %s" % (version1, mapper[res], version2)