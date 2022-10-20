from dict import ENG_TO_RU_DICT, RU_TO_ENG_DICT

lang = input('Choose the needed lang ("en" or "ru"): ')
output = ''

if lang == 'ru':
    user_input = input('Initial text: ')
    for letter in user_input:
        if letter in ENG_TO_RU_DICT:
            output += ENG_TO_RU_DICT[letter]
        else:
            output += letter
    print(output)

elif lang == 'en':
    user_input = input('Initial text: ')
    for letter in user_input:
        if letter in RU_TO_ENG_DICT:
            output += RU_TO_ENG_DICT[letter]
        else:
            output += letter
    print(output)

else: print(f"I don't know the language {lang}, try again")
