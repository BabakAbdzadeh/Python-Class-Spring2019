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


text_words = word_counter(wasteland_text)

text_words_duplicate = str(text_words[0])
text_words_noDuplicate = str(text_words[1])


wasteland_output.write(text_words_duplicate)
wasteland_output.write('\n')
wasteland_output.write(text_words_noDuplicate)
print(word_frequency(wasteland_text))



