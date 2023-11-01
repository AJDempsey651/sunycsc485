from sunycsc485.projects.hw13.hw13 import compute_complexity, evaluate_strength
import pytest


@pytest.mark.parametrize('complexity', [0])
def test_evaluate_strength_low(complexity):
    """Test that evaluate_strength will return false if passwords do not meet
    the strength threshold"""
    assert evaluate_strength(complexity) == False


@pytest.mark.parametrize('complexity', [50])
def test_evaluate_strength_high(complexity):
    """Test that evaluate_strength will return true is passwords meet the
     strength threshold"""
    assert evaluate_strength(complexity) == True


@pytest.mark.parametrize('passwords', ['password1', 'password2'])
def test_complexity_strength_low(passwords):
    """Test that compute_complexity will return 0 if there are no
    complexifiers"""
    assert compute_complexity(passwords) == 0.0


@pytest.mark.parametrize('passwords', ['123@#%', 'abcde@#$%^'])
def test_complexity_strength_high(passwords):
    """Test that compute_complexity will return 50.0 is there is an even
    number of complexifiers to other characters"""
    assert compute_complexity(passwords) == 50.0
