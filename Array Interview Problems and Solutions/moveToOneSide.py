def move_to_one_side(arr):
    if len(arr) < 1:
        return "length issues"

    read_stream = len(arr) - 1
    write_stream = len(arr) - 1

    while read_stream >= 0:
        if arr[read_stream] != 0:
            arr[write_stream] = arr[read_stream]
            write_stream -= 1

        read_stream -= 1

    while write_stream >= 0:
        arr[write_stream] = 0
        write_stream -= 1

    return arr


print(move_to_one_side([5, 6, 10, 0, 60, 61, 0, 90, 0]))
