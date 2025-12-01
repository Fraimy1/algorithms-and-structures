import pytest
from src.utils.generators import (rand_int_array, 
                                  nearly_sorted, 
                                  many_duplicates, 
                                  reverse_sorted,
                                  rand_float_array)
from src.core.errors import IncorrectInputError

def test_rand_int_array():
    # test seed
    seed = 42
    arr = rand_int_array(10, 0, 100, seed=seed)
    arr2 = rand_int_array(10, 0, 100, seed=seed)
    assert arr == arr2

    arr = rand_int_array(10, 0, 100, seed=seed, distinct=True)
    assert len(arr) == len(set(arr))
    
    arr = rand_int_array(10**6, 0, 100, seed=seed, distinct=False)
    assert len(arr) == 10**6
    assert all(0 <= n <= 100 for n in arr)
    
    with pytest.raises(IncorrectInputError):
        rand_int_array(-1, 0, 100)
    with pytest.raises(IncorrectInputError):
        rand_int_array(10, 100, 0)
    with pytest.raises(IncorrectInputError):
        rand_int_array(10, 0, 5, distinct=True)
    
    assert rand_int_array(0, 0, 0) == []

def test_nearly_sorted():
    seed = 42
    arr = nearly_sorted(10, 2, seed=seed)
    arr2 = nearly_sorted(10, 2, seed=seed)
    assert arr == arr2
    
    assert sorted(arr) == list(range(10))
    assert len(arr) == 10
    assert len(set(arr)) == 10

    with pytest.raises(IncorrectInputError):
        nearly_sorted(-1, 2)
    with pytest.raises(IncorrectInputError):
        nearly_sorted(10, -2)
    with pytest.raises(IncorrectInputError):
        nearly_sorted(10, 11)

    assert nearly_sorted(0, 0) == []

    arr = nearly_sorted(10**6, 2, seed=seed)
    assert len(arr) == 10**6
    assert len(set(arr)) == 10**6
    
    arr = nearly_sorted(100, 2, seed=seed)
    assert len(arr) == 100
    assert len(set(arr)) == 100



def test_many_duplicates():
    seed = 42
    arr = many_duplicates(10, 2, seed=seed)
    arr2 = many_duplicates(10, 2, seed=seed)
    assert arr == arr2
    
    assert len(arr) == 10
    assert len(set(arr)) == 2
    assert all(n in [0, 1] for n in arr)
    
    with pytest.raises(IncorrectInputError):
        many_duplicates(-1, 2)
    
    with pytest.raises(IncorrectInputError):
        many_duplicates(10, 11)
    
    assert many_duplicates(0, 0) == []

def test_reverse_sorted():
    arr = reverse_sorted(10)
    assert arr == list(range(10, 0, -1))
    assert len(arr) == 10
    assert len(set(arr)) == 10
    
    with pytest.raises(IncorrectInputError):
        reverse_sorted(-1)
    
    assert reverse_sorted(0) == []
    
    arr = reverse_sorted(10**6)
    assert len(arr) == 10**6

def test_rand_float_array():
    seed = 42
    arr = rand_float_array(10, 0.0, 1.0, seed=seed)
    arr2 = rand_float_array(10, 0.0, 1.0, seed=seed)
    assert arr == arr2
    
    assert len(arr) == 10
    assert all(0.0 <= n <= 1.0 for n in arr)
    
    with pytest.raises(IncorrectInputError):
        rand_float_array(-1, 0.0, 1.0)
    with pytest.raises(IncorrectInputError):
        rand_float_array(10, 1.0, 0.0)

    assert rand_float_array(0, 0, 1) == []