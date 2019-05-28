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
