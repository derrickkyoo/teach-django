import pytest

from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_home_reverse():
    assert reverse("pages:home") == "/"


def test_home_resolve():
    assert resolve("/").view_name == "pages:home"


def test_about_reverse():
    assert reverse("pages:about") == "/about/"


def test_about_resolve():
    assert resolve("/about/").view_name == "pages:about"
