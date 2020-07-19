import factory
import pytest


@pytest.fixture
def post():
    return PostFactory()


class PostFactory(factory.django.DjangoModelFactory):
    text = factory.Faker(
        "paragraph", nb_sentences=5, variable_nb_sentences=True
    )
