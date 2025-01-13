
def ubbi_word(word):
    # Check that input is a string
    if not isinstance(word, str):
        raise AttributeError("Input must be a string")
    
    # Check for uppercase letters
    if any(c.isupper() for c in word):
        raise ValueError("Input must be lowercase")
    
    # Check for non-ASCII characters
    if not word.isascii():
        raise ValueError("Input must contain only ASCII characters")
    
    if not one_character.isalpha():
        raise ValueError(f'{one_character} is illegal; stopping now')

    output = []
    for one_character in word:
        if one_character in 'aeiou':
            output.append('ub')
        output.append(one_character)
    return ''.join(output)    