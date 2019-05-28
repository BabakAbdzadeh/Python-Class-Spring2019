def quiz(input_string):
    i = 0

    output_string = ""
    while i != len(input_string):

        ascii_input = ord(input_string[i])
        if int(ascii_input) != 32 or int(ascii_input) != 121 or int(ascii_input) != 122:
            ascii_1char_out_put = int(ascii_input) + 2

        if ascii_input == 121:
            ascii_1char_out_put += 1
        if ascii_input == 122:
            ascii_1char_out_put = 97
        if ascii_input == 32:
            ascii_1char_out_put == ascii_input

        char_out_put = chr(ascii_1char_out_put)
        output_string = output_string + char_out_put
        # string_output_list = list(string_output)
        i += 1

    return output_string


print(quiz("abcz"))
