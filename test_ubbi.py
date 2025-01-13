from ubbi import ubbi_word

def test_simple_word():
    assert ubbi_word("dog") == "dubog"

def test_multiple_vowels():
    assert ubbi_word("see") == "subeube"

def test_no_vowels():
    assert ubbi_word("cry") == "cry"

def test_vowel_at_start():
    assert ubbi_word("eat") == "ubeubeat"

def test_consecutive_vowels():
    assert ubbi_word("moon") == "mubouboon"

def test_empty_string():
    assert ubbi_word("") == ""

def test_all_vowels():
    assert ubbi_word("aeiou") == "ubaubeubiuboubou"

def test_single_letter_vowel():
    assert ubbi_word("a") == "uba"

def test_single_letter_consonant():
    assert ubbi_word("z") == "z"
    