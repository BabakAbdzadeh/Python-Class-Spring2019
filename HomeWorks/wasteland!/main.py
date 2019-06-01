import itertools #its important
import re
from typing import List, Any

wasteland = open('wasteland.txt', mode="r")
wasteland_output = open('out_words_count.txt', mode='w')

wasteland_text = wasteland.read()


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


def word_frequency(input_string):
    pattern = "\w{2,}"
    input_words = re.findall(pattern, input_string)
    unique = []
    duplicate_count = []
    input_no_duplicate_dict = {}
    i = 0
    for words in range(len(input_words)):
        duplicate_pattern = str(input_words[words])
        if input_words[words] not in unique:
            unique.append(input_words[words])
            duplicate_count.append(0)
        while re.search(duplicate_pattern, input_string):
            # input_words.remove(input_words[words])
            input_string = re.sub(duplicate_pattern, " ", input_string, 1)
            i += 1
            # input_words.append(input_words[words])
        duplicate_count.append(i)
        i = 0
    duplicate_count_dictionary = dict(zip(unique, duplicate_count))
    # for words in unique:
    #     input_no_duplicate_dict[words] = {}
    #  for i in range(len(unique)):
    #      input_no_duplicate_dict[i] = duplicate_count[i]
    # input_no_duplicate_dict.update(duplicate_count: [])
    # for dict_member in range(len(input_no_duplicate_dict)):
    #     input_no_duplicate_dict[dict_member] = str(duplicate_count[dict_member])
    return duplicate_count_dictionary


text_words = word_counter(wasteland_text)

text_words_duplicate = str(text_words[0])
text_words_noDuplicate = str(text_words[1])


wasteland_output.write(text_words_duplicate)
wasteland_output.write('\n')
wasteland_output.write(text_words_noDuplicate)
print(word_frequency(wasteland_text))


