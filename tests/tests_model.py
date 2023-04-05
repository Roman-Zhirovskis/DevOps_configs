import pytest
from django.urls import reverse

from core.models import Category, Women


@pytest.mark.django_db
def test_women_str_method(women):
    assert str(women) == "Test Women"


@pytest.mark.django_db
def test_category_str_method(category):
    assert str(category) == "Test Category"
