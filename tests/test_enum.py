"""
test methods for get_data module enumerators
"""

from imports import BaseEnumerator, RestMethod


def test_base_enumerator_exists():
    """
    test that BaseEnumerator exists
    """
    assert BaseEnumerator


def test_base_enumerator_is_enumerator():
    """
    test that BaseEnumerator is enumerator
    """
    assert BaseEnumerator


def test_base_enumerator_has_class_method_values():
    """
    test that BaseEnumerator has class method `values` that returns a list
    """
    assert isinstance(BaseEnumerator.values(), list)


def test_base_enumerator_has_class_method_keys():
    """
    test that BaseEnumerator has class method `keys` that returns a list
    """
    assert isinstance(BaseEnumerator.keys(), list)


def test_rest_method_enumerator_exists():
    """
    test that get data RestMethod enumerator exists
    """
    assert RestMethod


def test_keys_rest_method_enumerator():
    """
    test that ResponseFormat keys are of type XML, JSON, CSV or HTML
    """
    for key in RestMethod.keys():
        assert key in ["GET", "POST"]
