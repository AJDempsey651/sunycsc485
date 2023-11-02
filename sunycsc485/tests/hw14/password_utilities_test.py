from sunycsc485.projects.hw14.password_utilities import (
    compute_complexity, evaluate_strength)
import pytest


@pytest.mark.parametrize('complexity', [0])
def evaluate_strength_test_low(complexity):
    """Test that evaluate_strength will return false if passwords
    do not meet the strength threshold"""
    assert evaluate_strength(complexity) == False


@pytest.mark.parametrize('complexity', [50])
def evaluate_strength_test_high(complexity):
    """Test that evaluate_strength will return true is passwords
    meet the strength threshold"""
    assert evaluate_strength(complexity) == True


@pytest.mark.parametrize('passwords', ['password1', 'password2'])
def test_complexity_0_strength(passwords):
    """Test that compute_complexity will return 0 if there are
    no complexifiers"""
    assert compute_complexity(passwords) == 0.0


@pytest.mark.parametrize('passwords', ['123@#%', 'abcde@#$%^'])
def test_complexity_50_strength(passwords):
    """Test that compute_complexity will return 50.0 is there is
    an even number of
    complexifiers to other characters"""
    assert compute_complexity(passwords) == 50.0
