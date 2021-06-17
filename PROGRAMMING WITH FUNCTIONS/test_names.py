from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Penelope", "Smith-Jones") == "Smith-Jones; Penelope"

def test_extract_family_name():
    assert extract_family_name("Smith-Jones; Penelope") == "Smith-Jones"

def test_extract_given_name():
    assert extract_given_name("Smith-Jones; Penelope") == "Penelope"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])