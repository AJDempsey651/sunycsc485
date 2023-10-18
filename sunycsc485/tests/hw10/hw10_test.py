from sunycsc485.projects.hw10.hw10 import is_it_a_fruit
import pytest


def test_fruit_is_apple():
    """test_fruit_is_apple tests to see if 'apple' is in is_it_a_fruit"""
    assert is_it_a_fruit('apple') == True


def test_fruit_is_pear():
    """test_fruit_is_pear tests to see if 'pear' is in is_it_a_fruit"""
    assert is_it_a_fruit('pear') == True


def test_fruit_is_bananna():
    """test_fruit_is_bananna tests to see if 'bananna' is in is_it_a_fruit"""
    assert is_it_a_fruit('bananna') == True


def test_fruit_is_grape():
    """test_fruit_is_grape tests to see if 'grape' is in is_it_a_fruit"""
    assert is_it_a_fruit('grape') == True


def test_integer():
    """test_integer tests to make sure that there are no integers in
    is_it_a_fruit"""
    assert is_it_a_fruit(5) == False


def test_banana_spelling():
    """test_banana_spelling tests to make sure the correct spelling of banana
     will not return True"""
    assert is_it_a_fruit('banana') == False


def test_random_string():
    """test_random_string tests to make sure a random input as a string will
    not return True"""
    assert is_it_a_fruit('wrench') == False


def test_multiple_inputs():
    """test_multiple_inputs tests to make sure that multiple inputs as strings
     will return with a TypeError"""
    with pytest.raises(Exception) as e:
        is_it_a_fruit('apple', 'pear')
    assert e.type == TypeError
