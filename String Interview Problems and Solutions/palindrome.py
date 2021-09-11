# not so great way


def palindrome_not_so_great_way(s):
    reverse = ""
    for i in reversed(range(len(s))):
        reverse += s[i]
    if s == reverse:
        return "Yes"
    return "No"


print(palindrome_not_so_great_way("HAHAH"))


# one of the great way


def palindrome_not_so_great_way(s):
    reverse = []
    for i in reversed(range(len(s))):
        reverse.append(s[i])
    if s == "".join(reverse):
        return "Yes"
    return "No"


print(palindrome_not_so_great_way("HAHAH"))
