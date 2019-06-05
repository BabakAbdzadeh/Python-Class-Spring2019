def write_dic_for_out_put(input_dic, out_put_variable, with_number_counter_y_n, before_first_key_pattern
                          , before_sec_key_pattern, after_sec_key_pattern):
    for i in range(len(input_dic)):
        x = list(input_dic.items())
        z = x[i]
        a = z[0]
        b = str(z[1])
        if with_number_counter_y_n == "yes":
            out_put_variable.write(str(i + 1) + before_first_key_pattern)
        else:
            out_put_variable.write(before_first_key_pattern)
        out_put_variable.write(a)
        out_put_variable.write(before_sec_key_pattern)
        out_put_variable.write(b)
        out_put_variable.write(after_sec_key_pattern)
