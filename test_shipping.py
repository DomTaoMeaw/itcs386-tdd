
import pytest
from shipping import shipping_fee


# Rule 1: Weight must be more than 0 kg.
@pytest.mark.parametrize("weight", [0, -1, -0.5])
def test_invalid_weight_is_rejected(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)


# Rule 2: A parcel of up to 1 kg costs 40 baht.
@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),
    (1, 40),
])
def test_up_to_one_kg_costs_40(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 3: More than 1 kg and up to 5 kg costs 60 baht.
@pytest.mark.parametrize("weight, expected", [
    (1.1, 60),
    (3, 60),
    (5, 60),
])
def test_over_one_to_five_kg_costs_60(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 4: Every started kilogram above 5 kg adds 10 baht.
@pytest.mark.parametrize("weight, expected", [
    (5.2, 70),
    (6, 70),
    (6.1, 80),
    (7.5, 90),
])
def test_over_five_kg_costs_extra(weight, expected):
    assert shipping_fee(weight) == expected
