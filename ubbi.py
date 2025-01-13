def ubbi_word(word):
    output = []

    for one_character in word:
        if not one_character.isalpha():
            raise ValueError(f'{one_character} is illegal; stopping now')
        if one_character in 'aeiou':
            output.append('ub')
        output.append(one_character)

    return ''.join(output)
    