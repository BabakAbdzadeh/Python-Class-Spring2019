import re


wasteland = open('wasteland.txt', mode="r")
wasteland_output = open('out_words_count.txt', mode='w')

wasteland_text = wasteland.read()


def word_counter(input_string):
    pattern = "\w{2,}"
    input_words = re.findall(pattern, input_string)
    words_count = len(input_words)
    # remove repeating
    unique = []
    i = 0
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
