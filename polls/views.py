
from .models import Post
from django.views.generic import ListView, DetailView
 
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-id'
    paginate_by = 5
 
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
