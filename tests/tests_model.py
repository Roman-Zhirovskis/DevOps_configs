import pytest


@pytest.mark.django_db
def test_women_str_method(women):
    assert str(women) == "Test Women"


@pytest.mark.django_db
def test_category_str_method(category):
    assert str(category) == "Test Category"


@pytest.mark.django_db
def test_category_str_method1(category):
    assert str(category) == "Test Category2"
