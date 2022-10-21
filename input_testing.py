from dict import *


def letters_transform(user_input):
    output = ''
    if user_input[0] in ENG_TO_RU_DICT:
        for letter in user_input:
            if letter in ENG_TO_RU_DICT:
                output += ENG_TO_RU_DICT[letter]
            else:
                output += letter
        return output

    elif user_input[0] in RU_TO_ENG_DICT:
        for letter in user_input:
            if letter in RU_TO_ENG_DICT:
                output += RU_TO_ENG_DICT[letter]
            else:
                output += letter
        return output

    else:
        return user_input
