from sunycsc485.projects.hw12.hw12 import compute_complexity
import pytest


@pytest.mark.parametrize('passwords', ['password1', 'password2'])
def test_complexifiers(passwords):
    assert compute_complexity(passwords) == 0.0
