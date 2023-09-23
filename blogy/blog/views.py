from django.views import generic
from .models import Post
from django.shortcuts import render
from django.utils.translation import gettext as _

# def acceuil(request):
#   return render(request, 'index.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'postlist.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
