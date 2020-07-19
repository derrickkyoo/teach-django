import pytest
from pytest_django.asserts import assertContains

# from django.test import RequestFactory
from django.urls import reverse

from ..views import HomePageView, AboutPageView

pytestmark = pytest.mark.django_db


def test_home_page_status(rf):
    url = reverse("pages:home")
    request = rf.get(url)
    callable_obj = HomePageView.as_view()
    response = callable_obj(request)
    assertContains(response, "Homepage")


def test_about_page_status(rf):
    url = reverse("pages:about")
    request = rf.get(url)
    callable_obj = AboutPageView.as_view()
    response = callable_obj(request)
    assertContains(response, "About")
