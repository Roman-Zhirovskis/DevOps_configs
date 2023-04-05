import pytest

from core.models import Category, Women


@pytest.fixture
def women():
    return Women.objects.create(
        title="Test Women",
        slug="test-women",
        content="Test content",
        photo="test.jpg",
        is_published=True,
        cat=Category.objects.create(name="Test Category", slug="test-category"),
    )


@pytest.fixture
def category():
    return Category.objects.create(name="Test Category", slug="test-category")
