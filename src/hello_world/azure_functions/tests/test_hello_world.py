from ..hello_world import calculate_vowels_in_name

def test_calculate_vowels_in_name():
    name = "Hannes De Smet"
    assert calculate_vowels_in_name(name) == 4