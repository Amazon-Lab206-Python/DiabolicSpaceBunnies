'''# input
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
# output
new_list = ['hello', 'world']


def new_list = []
    word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
        for char = x
        if char val == x
        list val
        insert val into new_list'''


def find_character(word_list, char):
    new_list = []
    for idx in range(0, len(word_list)):

        if word_list[idx].find(char) >= 0:
            '''where is char defined? and why ! = -1?'''
            new_list.append(word_list[idx])

    print new_list


test_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
find_character(test_list, 'a')
