
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def home(request):
   return render(request, 'home.html',{})
#class P(models.Model):
 #   title = models.CharField(max_length=255)
  #  author = models.ForeignKey(User, on_delete=models.CASCADE)
   # body = models.TextField()/
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class Home(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']
    #ordering = ['-id']
class Article(DetailView):
    model = Post
    template_name = "Articles_details.html"
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = '__all__'
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
    #fields = '__all__'
