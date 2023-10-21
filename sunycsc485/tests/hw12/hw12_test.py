from sunycsc485.projects.hw12.hw12 import compute_complexity
import pytest


@pytest.mark.parametrize('compute_complexity', ['~', '@', '#', '$', '%',
                                                '^', '&', '-', '_', '+', '='])
def test_complexifiers(compute_complexity):
    assert (compute_complexity == '~' or '@' or '#' or '$' or '%' or '^'
            or '&' or '-' or '_' or '+' or '=')
