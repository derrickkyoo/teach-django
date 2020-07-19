import pytest

from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_post_reverse():
    assert reverse("posts:list") == "/posts/"


def test_post_resolve():
    assert resolve("/posts/").view_name == "posts:list"
