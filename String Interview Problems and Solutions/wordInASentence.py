def reverse_sentence(given_string):
    str_array = given_string.split(" ")
    rev_str_array = []

    for s in str_array:
        rev_str_array.insert(0, s)

    # reversed_string = ""
    # for s in rev_str_array:
    #     reversed_string = reversed_string + s + " "

    reversed_string = " ".join(rev_str_array)

    return reversed_string


print(reverse_sentence("Hello World"))
