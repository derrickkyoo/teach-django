import pytest

from django.urls import reverse

from pytest_django.asserts import assertContains

from ..models import Post
from ..views import PostListView
from .factories import post

pytestmark = pytest.mark.django_db


def test_post_list_view_expanded(rf):
    url = reverse("posts:list")
    request = rf.get(url)
    callable_obj = PostListView.as_view()
    response = callable_obj(request)
    assertContains(response, "Posts")


def test_post_list_view(rf):
    url = reverse("posts:list")
    request = rf.get(url)
    response = PostListView.as_view()(request)
    assertContains(response, "Posts")
