from dict import *


def letters_transform(user_input, lang='ru'):
    output = ''
    if lang == 'ru':
        for letter in user_input:
            if letter in ENG_TO_RU_DICT:
                output += ENG_TO_RU_DICT[letter]
            else:
                output += letter
        return output
    elif lang == 'en':
        for letter in user_input:
            if letter in RU_TO_ENG_DICT:
                output += RU_TO_ENG_DICT[letter]
            else:
                output += letter
        return output
    else:
        return "Ой! Что-то пошло не так :("


if __name__ == '__main__':
    user_in = 'привет z ntcnjdsq cjj,otybt lkz <jnf ^))'
    print(letters_transform(user_input=user_in))
