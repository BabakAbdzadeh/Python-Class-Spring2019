import glob
import re

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
# 1 find no parent files :

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
#
# 2 find files without children:
no_children_var = open('no_children.txt', mode='w')
list_no_children = []
list_with_children = []
txt_as_string = ' '.join(files_txt_list)
for items in file_names:
    pattern_for_search = str(items)
    if re.search(pattern_for_search, txt_as_string):
        list_with_children.append(items)
    else:
        list_no_children.append(items)

print(len(list_no_children))
print(list_no_children)

for i in range(len(list_no_children)):
    no_children_var.write(str(i))
    no_children_var.write('.')
    no_children_var.write(' ')
    no_children_var.write(list_no_children[i])
    no_children_var.write('\n')
# Done

# Q3:
count = 0
longest = 0
index_no_parent = 0
generation_test_list = []
generation_real_list = []
while index_no_parent != len(no_parent_file):
    father = no_parent_file[index_no_parent]
    generation_test_list.append(father)
    for z in files_txt_list:
        if re.search(father, txt_as_string):
            count += 1
            children = re.findall(father, txt_as_string)
            generation_test_list.append(children)
            father = children[0]
        else:
            1
    if count >= longest:
        longest = count
        generation_real_list = generation_test_list
    else:
        1
    index_no_parent += 1

print(longest)
print(len(generation_real_list))
# print(generation_real_list)
