from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post


class BlogListView(ListView):
    """Blog List View"""

    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    """Blog Detail View"""

    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    """Blog Create View"""

    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    # Can set this if you wanted one form to redirect
    # somewhere other than the get_absolute_url method
    # success_url = reverse_lazy("home")


class BlogUpdateView(UpdateView):
    """Blog Update View"""

    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    """Blog Delete View"""

    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
