# the longest substring should not have any duplicate characters


def longest_substring(s):
    global_max = 0
    start = 0
    diary = {}
    substring = ""

    for green_end in range(len(s)):
        if s[green_end] in diary:
            start = max(start, diary[s[green_end]] + 1)
        diary[s[green_end]] = green_end

        global_max = max(global_max, (green_end - start + 1))

    d_start = start
    for i in range(global_max):
        substring += s[d_start]
        d_start += 1

    return global_max, substring


substring_length, substring = longest_substring("ABCDABCEF")
print(substring_length, substring)
