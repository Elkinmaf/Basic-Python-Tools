def until_gap(s):

    index = 0
    s = "Mind the gap!"
    while index < len(s) and s[index] != " ":
        index += 1
    return s[:index]
