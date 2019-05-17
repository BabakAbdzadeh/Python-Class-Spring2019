def quiz(input_string):
    i = 0

    string_output = ""
    while i != len(input_string):
        i = 0
        ascii_input = ord(input_string(i))
        if ascii_input != 32 or ascii_input != 121 or ascii_input != 122:
            ascii_1char_out_put = ascii_input + 2

        if ascii_input == 121:
            ascii_1char_out_put += 1
        if ascii_input == 122:
            ascii_1char_out_put = 97
        if ascii_input == 32:
            ascii_1char_out_put == ascii_input

        char_out_put = chr(ascii_1char_out_put)
        string_output = string_output + char_out_put
        # string_output_list = list(string_output)
        i += 1

    return string_output


print(quiz("a"))
