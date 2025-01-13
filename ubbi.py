def ubbi_word(word):
    output = []

    for one_character in word:
        if one_character in 'aeiou':
            output.append('ub')
        output.append(one_character)

    return ''.join(output)
    