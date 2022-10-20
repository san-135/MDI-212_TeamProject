from dict import RU_TO_ENG_DICT, ENG_TO_RU_DICT


def letters_transform(user_input):
    output = ''
    for letter in user_input:
        if letter in ENG_TO_RU_DICT:
            output += ENG_TO_RU_DICT[letter]
        elif letter in RU_TO_ENG_DICT:
            output += RU_TO_ENG_DICT[letter]
        else:
            output += letter
    return output


if __name__ == '__main__':
    user_in = 'привет z ntcnjdsq cjj,otybt lkz <jnf ^))'
    print(letters_transform(user_input=user_in))
