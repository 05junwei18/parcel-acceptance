import pytest
from src.parcel_fee import delivery_fee

## Band 1( 1g - 1000g) inclusive fee = 500

def test_weight_at_lower_boundary_1g_returns_500():
    weight_grams = 1
    result = delivery_fee(weight_grams)
    assert result == 500    # 1st test case: weight = 1g, expected fee = 500


def test_weight_within_first_band_500g_returns_500():
    weight_grams = 500
    result = delivery_fee(weight_grams)
    assert result == 500   # 2nd test case: weight = 500g, expected fee = 500


def test_weight_at_upper_boundary_1000g_returns_500():
    weight_grams = 1000
    result = delivery_fee(weight_grams)
    assert result == 500    # 3rd(f) test case: weight = 1000g, expected fee = 500, parcel fee at 1000g will be at the over boundary of the first weight band


## Band 2( 1001g - 20000g) inclusive fee = 1000

def test_weight_at_lower_boundary_1001g_returns_1000():
    weight_grams = 1001
    result = delivery_fee(weight_grams)
    assert result == 1000   # 4th test case: weight = 1001g, expected fee = 1000

def test_weight_within_second_band_5000g_returns_1000():
    weight_grams = 5000
    result = delivery_fee(weight_grams)
    assert result == 1000   # 5th test case: weight = 5000g, expected fee = 1000

def test_weight_at_upper_boundary_20000g_returns_1000():
    weight_grams = 20000
    result = delivery_fee(weight_grams)
    assert result == 1000   # 6th test case: weight = 20000g, expected fee = 1000


## Invalid weight values

def test_weight_zero_raises_value_error():
    weight_grams = 0
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)   # 7th test case: weight = 0g, expected to raise ValueError

def test_weight_negative_raises_value_error():
    weight_grams = -1
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)   # 8th test case: weight = -1g, expected to raise ValueError

def test_weight_above_upper_boundary_20001g_raises_value_error():
    weight_grams = 20001
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)   # 9th test case: weight = 20001g, expected to raise ValueError

## Invalid weight types

def test_weight_non_integer_raises_type_error():
    weight_grams = 500.5
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)   # 10th test case: weight = 500.5g, expected to raise TypeError


def test_weight_boolean_true_raises_type_error():
    weight_grams = True
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)   # 11th test case: weight = True, expected to raise TypeError

def test_weight_string_raises_type_error():
    weight_grams = "1000"
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)   # 12th test case: weight = "1000", expected to raise TypeError, 1000 is a string and not an integer, so it should raise TypeError

