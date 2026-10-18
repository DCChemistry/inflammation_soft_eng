"""Tests for statistics functions within the Trial layer."""
from inflammation.trial import Patient


def test_data_mean():
    """Test mean function works for array of zeros and positive integers."""
    test_data = [1, 3, 5]
    expected_result = 3.
    patient = Patient(0, test_data)
    assert patient.data_mean == expected_result


def test_data_max():
    test_data = [1, 3, 5]
    expected_result = 5.
    patient = Patient(0, test_data)
    assert patient.data_max == expected_result


def test_data_min():
    test_data = [1, 3, 5]
    expected_result = 1.
    patient = Patient(0, test_data)
    assert patient.data_min == expected_result
