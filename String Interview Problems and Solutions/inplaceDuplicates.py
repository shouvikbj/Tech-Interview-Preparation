def remove_duplicates_inplace(s):
    s = list(s)

    my_set = set([])

    write_stream = 0
    read_stream = 0

    while read_stream < len(s):
        if s[read_stream] not in my_set:
            my_set.add(s[read_stream])
            s[write_stream] = s[read_stream]
            write_stream += 1
        read_stream += 1

    for i in range(write_stream, len(s)):
        s[i] = "\0"

    s = "".join([str(i) for i in s if s != "\0"])

    return s


print(remove_duplicates_inplace("DADABACDA"))
