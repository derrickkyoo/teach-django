import pytest

import factory
import factory.fuzzy

from helloworld.users.tests.factories import UserFactory
from ..models import Post


@pytest.fixture
def post():
    return PostFactory()


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    text = factory.Faker(
        "paragraph", nb_sentences=5, variable_nb_sentences=True
    )
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Post
