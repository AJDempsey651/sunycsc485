from csc485.projects.hw12.hw12 import is_it_a_fruit
import pytest
@pytest.mark.parametrize('fruit_candidate', ['apple', 'pear', 'bananna', 'grape'])

def test_good_key(fruit_candidate):
    this_fruit = fruit_candidate
    assert is_it_a_fruit(this_fruit)