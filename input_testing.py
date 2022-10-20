from dict import *


def letters_transform(lang='ru', user_input=''):
    output = ''
    if lang == 'ru':
        # user_input = input('Initial text: ')
        for letter in user_input:
            if letter in ENG_TO_RU_DICT:
                output += ENG_TO_RU_DICT[letter]
            else:
                output += letter
        return output

    elif lang == 'en':
        # user_input = input('Initial text: ')
        for letter in user_input:
            if letter in RU_TO_ENG_DICT:
                output += RU_TO_ENG_DICT[letter]
            else:
                output += letter
        return output

    else: print(f"I don't know the language {lang}, try again")


language = input('Choose the needed lang ("en" or "ru"): ')
user_in = input('Initial text: ')
letters_transform(language, user_in)
