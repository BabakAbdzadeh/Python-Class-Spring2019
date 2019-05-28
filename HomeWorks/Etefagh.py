data = [50.3, 338.4, 626.5, 959.4, 1317.9, 1716.7, 2134.3, 2565.5, 3085.6, 3626.7]


def duration_calculator(data_in):
    duration_calc = []
    i = 0
    while i + 1 != len(data_in):
        duration_parameter = data_in[i + 1] - data_in[i]
        duration_calc.append(duration_parameter)
        i += 1
    return duration_calc


duration = duration_calculator(data)
print(duration)


def duration_description(data_in):
    i = 0
    t1 = 300
    t2 = 400
    description = ""
    len_data_in_variable = len(data_in)
    while i != len_data_in_variable:
        comp_variable = data_in.pop(0)
        if comp_variable < t1:
            describe_char = "S"
        elif comp_variable >= t2:
            describe_char = "L"
        else:
            describe_char = "M"
        description = description + describe_char
        i += 1
    return description


duration_describe = duration_description(duration)
print(duration_describe)
