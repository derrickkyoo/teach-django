from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
)

app_name = "posts"
urlpatterns = [
    path("<int:pk>/edit", PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("", PostListView.as_view(), name="list"),
]
