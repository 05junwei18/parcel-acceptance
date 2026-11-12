import pytest 
from parcel_acceptance import is_parcel_accepted

## Test cases for the is_parcel_accepted function
def test_weight_at_lower_boundary_1g_is_accepted():
    weight_grams = 1
    length_cm = 1
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is True   # 1st test case: weight = 1g, length = 1cm, expected acceptance = True

def test_nominal_weight_and_length_returns_true():
    weight_grams = 5000
    length_cm = 100
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is True   # 2nd test case: weight = 5000g, length = 100cm, expected acceptance = True

def test_maximum_weight_and_length_returns_true():
    weight_grams = 20000
    length_cm = 200
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is True   # 3rd(f) test case: weight = 20000g, length = 200cm, expected acceptance = True,, failed cause the length

## Invalid weight/ length values outside the service range

def test_zero_weight_returns_false():
    weight_grams = 0
    length_cm = 100
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is False   # 4th test case: weight = 0g, length = 100cm, expected acceptance = False


def test_zero_length_returns_false():
    weight_grams = 1000
    length_cm = 0
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is False   # 5th test case: weight = 1000g, length = 0cm, expected acceptance = False

def test_weight_above_upper_boundary_returns_false():
    weight_grams = 20001
    length_cm = 100
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is False   # 6th test case: weight = 20001g, length = 100cm, expected acceptance = False

def test_length_above_upper_boundary_returns_false():
    weight_grams = 1000
    length_cm = 201
    result = is_parcel_accepted(weight_grams, length_cm)
    assert result is False   # 7th test case: weight = 1000g, length = 201cm, expected acceptance = False

## negative weight/ length values

def test_negative_weight_raises_value_error():
    weight_grams = -1
    length_cm = 100
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)   # 8th test case: weight = -1g, length = 100cm, expected acceptance = False


def test_negative_length_raises_value_error():
    weight_grams = 1000
    length_cm = -1
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)   # 9th test case: weight = 1000g, length = -1cm, expected acceptance = False


## invalid data types for weight/ length values

def test_boolean_weight_raises_type_error():
    weight_grams = True
    length_cm = 100
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)   # 10th test case: weight = True, length = 100cm, expected acceptance = False

def test_boolean_length_raises_type_error():
    weight_grams = 1000
    length_cm = False
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)   # 11th test case: weight = 1000g, length = False, expected acceptance = False

def test_float_weight_raises_type_error():
    weight_grams = 500.5
    length_cm = 100
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)   # 12th test case: weight = 500.5g, length = 100cm, expected acceptance = False


def test_float_length_raises_type_error():
    weight_grams = 1000
    length_cm = 100.5
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)   # 13th test case: weight = 1000g, length = 100.5cm, expected acceptance = False

def test_string_weight_raises_type_error():
    weight_grams = "1000"
    length_cm = 100
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)   # 14th test case: weight = "1000", length = 100cm, expected acceptance = False 