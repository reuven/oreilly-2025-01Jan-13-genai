def ubbi_word(word):
    output = ''

    for one_character in word:
        if one_character in 'aeiou':
            output.append('ub')
        output.append(one_character)

    return ''.join(output)

ubbi_word('hello')

import pytest

def test_converts_vowels_to_ubbi():
    assert ubbi_word('hello') == 'hubellubo'

def test_handles_empty_string():
    assert ubbi_word('') == ''

def test_handles_no_vowels():
    assert ubbi_word('rhythm') == 'rhythm'

def test_handles_all_vowels():
    assert ubbi_word('aeiou') == 'ubaubeioubu'

def test_handles_mixed_case():
    assert ubbi_word('HeLLo') == 'HubeLLubo'