from ubbi import ubbi_word

def test_simple_word():
    assert ubbi_word("dog") == "dubog"

def test_multiple_vowels():
    assert ubbi_word("see") == "subeube"

def test_no_vowels():
    assert ubbi_word("cry") == "cry"

def test_vowel_at_start():
    assert ubbi_word("eat") == "ubeubat"

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


from ubbi import ubbi_word
import pytest

# Original tests remain...

def test_rejects_non_string():
    with pytest.raises(AttributeError):
        ubbi_word(42)
    with pytest.raises(AttributeError):
        ubbi_word(None)

def test_rejects_uppercase():
    with pytest.raises(ValueError):  # or whatever error you decide to raise
        ubbi_word("Dog")

def test_rejects_spaces():
    with pytest.raises(ValueError):
        ubbi_word("hot dog")

def test_rejects_punctuation():
    with pytest.raises(ValueError):
        ubbi_word("hello!")

def test_rejects_whitespace():
    with pytest.raises(ValueError):
        ubbi_word("dog\n")
    with pytest.raises(ValueError):
        ubbi_word("\tcat")

def test_long_string():
    # Test with a longer string to ensure performance
    long_input = "mississippi" * 1000
    result = ubbi_word(long_input)
    assert "ubissubi" in result  # verify a small portion is correct
    assert len(result) > len(long_input)  # basic length check

def test_non_ascii():
    with pytest.raises(ValueError):
        ubbi_word("café")    