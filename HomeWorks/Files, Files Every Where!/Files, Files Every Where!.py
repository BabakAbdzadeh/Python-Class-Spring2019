import glob
import re
import os

# putting all file names into a list:
list_of_files = glob.glob('./files/*.txt')
file_name_as_string = ''.join(list_of_files)
pattern = '\d+.txt'
file_name_txt = re.findall(pattern, file_name_as_string)
file_names = re.findall('\d+', file_name_as_string)
# done


# putting all files texts into a list with parallel index with file name list:
files_txt_list = []
for i in file_name_txt:
    index_var = file_name_txt.index(i)
    txt_open_directory = open('./files/' + file_name_txt[index_var], mode='r')

    txt = txt_open_directory.read()
    if txt == 0:
        files_txt_list.append('0')
    else:
        files_txt_list.append(txt)

# done


# making a dict from this two list:
files_dict = dict(zip(file_names, files_txt_list))


# done
#
# 1 find no parent file :

# Get a list of keys from dictionary which has the given value
def get_keys_by_value(dict_of_elements, value_to_find):
    list_of_keys = list()
    list_of_items = dict_of_elements.items()
    for item in list_of_items:
        if item[1] == value_to_find:
            list_of_keys.append(item[0])
    return list_of_keys


no_parent_file = get_keys_by_value(files_dict, '0')

print(no_parent_file)

# Done
