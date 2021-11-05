#!/usr/bin/env python3

import random
from dice_dict import dicelist

word_count = int(input("Number of words for password?\n"))

# Takes number of desired words and outputs a list of diceware codes
def num_gen(n):
    code_list = []

    for i in range(n):
        code = ""
        for i in range(5):
            code = code + str(random.randint(1,6))
        code_list.append(code)
    return code_list

# Takes diceware code list and translates to words
def code_convert(list_input):
    word_list = []

    for i in list_input:
        word_list.append(dicelist[i])
    return ' '.join(word_list)

print(code_convert(num_gen(word_count)))
