import itertools  # its important
import re
from typing import List, Any

wasteland = open('wasteland.txt', mode="r")
wasteland_output = open('out_words_count.txt', mode='w')
wasteland_outMostFrequent = open('out_most_frequent.txt', mode='w')
wasteland_capital_counter = open('out_capital_words.txt', mode='w')
wasteland_text = wasteland.read()


# 1
def word_counter(input_string):
    pattern = "\w{2,}"
    input_words = re.findall(pattern, input_string)
    words_count = len(input_words)
    # remove repeating
    unique = []

    for words in range(len(input_words)):
        if input_words[words] not in unique:
            unique.append(input_words[words])
    words_without_duplicate = len(unique)

    return words_count, words_without_duplicate


text_words = word_counter(wasteland_text)

text_words_duplicate = str(text_words[0])
text_words_noDuplicate = str(text_words[1])
wasteland_output.write(text_words_duplicate)
wasteland_output.write('\n')
wasteland_output.write(text_words_noDuplicate)


# 2
def word_frequency(input_string):
    pattern = "\w{2,}"
    input_words = re.findall(pattern, input_string)
    # unique = []
    # duplicate_count = []
    counts = {}
    for word in input_words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    # i = 0
    # for words in range(len(input_words)):
    #     duplicate_pattern = str(input_words[words])
    #     if input_words[words] not in unique:
    #         unique.append(input_words[words])
    #         duplicate_count.append(0)
    #     while re.search(duplicate_pattern, input_string):
    #
    #         input_string = re.sub(duplicate_pattern, "", input_string, 1)
    #         i += 1
    #
    #     duplicate_count.append(i)
    #     i = 0
    # duplicate_count_dictionary = dict(zip(unique, duplicate_count))

    return counts


# 3
def max_values_of_frequency(input_string):
    max_value_list = []
    max_keys_list = []
    i = 0
    dic = word_frequency(input_string)
    while i != 10:
        max_value_dic = max(dic.values())
        max_value_list.append(max_value_dic)
        max_keys = [k for k, v in dic.items() if v == max_value_dic]
        max_as_string = ''.join(
            max_keys)  # we need to convert it to string because it is list and we appent a list into another list ,
        # because of that we cant convert to list into a dic

        del dic[max_as_string]
        max_keys_list.append(max_as_string)
        i += 1
    max_value_dic_return = dict(zip(max_keys_list, max_value_list))
    return max_value_dic_return


# writing in output for question 3:
#
# ******* function version with multiple inputs ************
#
def write_dic_for_out_put(input_dic, out_put_variable, with_number_counter_y_n, before_first_key_pattern
                          , before_sec_key_pattern, after_sec_key_pattern):
    for i in range(len(input_dic)):
        x = list(input_dic.items())
        z = x[i]
        a = z[0]
        b = str(z[1])
        if with_number_counter_y_n == "yes":
            out_put_variable.write(str(i + 1) + before_first_key_pattern)
        elif with_number_counter_y_n == "no":
            out_put_variable.write(before_first_key_pattern)
        out_put_variable.write(a)
        out_put_variable.write(before_sec_key_pattern)
        out_put_variable.write(b)
        out_put_variable.write(after_sec_key_pattern)

# @@@@ first version function (2 inputs for input/out var) @@@@@@@

# def write_dic_for_out_put(input_dic, out_put_variable,):
#     for i in range(len(input_dic)):
#         x = list(input_dic.items())
#         z = x[i]
#         a = z[0]
#         b = str(z[1])
#         out_put_variable.write(str(i + 1) + ".")
#         out_put_variable.write(a)
#         out_put_variable.write("  ")
#         out_put_variable.write(b)
#         out_put_variable.write('\n')

# ******* first version ************
#
#
# for i in range(len(max_values_of_frequency(wasteland_text))):
#     x = list(max_values_of_frequency(wasteland_text).items())
#     z = x[i]
#     a = z[0]
#     b = str(z[1])
#     wasteland_outMostFrequent.write(str(i + 1) + ".")
#     wasteland_outMostFrequent.write(a)
#     wasteland_outMostFrequent.write("  ")
#     wasteland_outMostFrequent.write(b)
#     wasteland_outMostFrequent.write('\n')


write_dic_for_out_put(max_values_of_frequency(wasteland_text), wasteland_outMostFrequent, "yes", ".", "  ", '\n')


# 4
def top_five_long(input_string):
    list_of_keys = list(word_frequency(input_string).keys())
    len_var = []
    for i in range(len(list_of_keys)):
        len_var.append(int(len(list_of_keys[i])))

    len_list = []

    for i in range(0, 5):
        len_list.append(max(len_var))
        len_var.remove(max(len_var))

    min_characters_in_top_long = str(min(len_list))
    pattern = "\w{" + str(min_characters_in_top_long) + ",}"
    longest_words = re.findall(pattern, wasteland_text)

    frequency_dic = word_frequency(wasteland_text)
    time_keys_repeated = []
    for i in range(0, 5):
        search_keys = str(longest_words[i])
        time_keys_repeated.append(frequency_dic[search_keys])
    topfive_longchar_dictionary = dict(zip(longest_words, time_keys_repeated))
    return topfive_longchar_dictionary


# 5
def capital_counter(input_string):
    pattern = "[A-Z]+?[A-Z]+|[A-Z]+?[a-z]+"
    capital_words_list = re.findall(pattern, input_string)
    counts = {}
    for word in capital_words_list:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts


write_dic_for_out_put(capital_counter(wasteland_text), wasteland_capital_counter, "no", "", " (", ")\n")


