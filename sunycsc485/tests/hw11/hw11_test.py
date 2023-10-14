from csc485.projects.hw11.hw11 import get_formal_name
import pytest

def test_fruit_key_apple():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('apple') == ('Malus domestica')

def test_fruit_key_banana():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('banana') == 'Musa acuminata'

def test_fruit_key_orange():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('orange') == 'Citrus × sinensis'

def test_fruit_key_strawberry():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('strawberry') == 'Fragaria × ananassa'

def test_fruit_key_grape():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('grape') == 'Vitis vinifera'

def test_fruit_key_pineapple():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('pineapple') == 'Ananas comosus'

def test_fruit_key_mango():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('mango') == 'Mangifera indica'

def test_fruit_key_blueberry():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('blueberry') == 'Vaccinium corymbosum'

def test_fruit_key_peach():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('peach') == 'Prunus persica'

def test_fruit_key_watermelon():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('watermelon') == 'Citrullus lanatus'

def test_fruit_key_cherry():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('cherry') == 'Prunus avium'

def test_fruit_key_pear():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('pear') == 'Pyrus'

def test_fruit_key_plum():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('plum') == 'Prunus domestica'

def test_fruit_key_raspberry():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('raspberry') == 'Rubus idaeus'

def test_fruit_key_kiwi():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('kiwi') == 'Actinidia deliciosa'

def test_fruit_key_lemon():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('lemon') == 'Citrus limon'

def test_fruit_key_avocado():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('avocado') == 'Persea americana'

def test_fruit_key_pomegranate():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('pomegranate') == 'Punica granatum'

def test_fruit_key_cranberry():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('cranberry') == 'Vaccinium macrocarpon'

def test_fruit_key_grapefruit():
    """Test to ensure that the correct key returns the correct value"""
    assert get_formal_name('grapefruit') == 'Citrus × paradisi'

def test_multiple_arguments():
    """Test that if more than one positional arguements are given it will result in a TypeError"""
    with pytest.raises(Exception) as e:
        get_formal_name(('apple') == 'Malus domestica', ('banana') == 'Musa acuminata')
    assert e.type == TypeError

def test_key_error():
    """Test that a positional argument(key) being given that is not in the dictionary will return a KeyError"""
    with pytest.raises(Exception) as e:
        get_formal_name('blackberry') == ('Rubus fruticosus')
    assert e.type == KeyError

def test_key_does_not_equal():
    """Test that a positional argument(key) will only return it's assigned value and not another value in the dictionary"""
    assert get_formal_name('apple') != ('Musa acuminata')

def test_testcase_difference():
    """Test that a change in the structure of the key will result in a key error"""
    assert get_formal_name('Apple') == ('Malus domestica')
