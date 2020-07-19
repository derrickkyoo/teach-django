from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def title(self):
        return "Post List"
