from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def title(self):
        return "Post List"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    fields = (
        "title",
        "text",
    )
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:list")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = (
        "title",
        "text",
    )
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
