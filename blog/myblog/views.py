from django.db.models.fields import files
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = "posts"
    ordering = ['-id']

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'Все категории'
        context['categories'] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['active'] = stuff.category.name
        context['categories'] = Category.objects.all()
        context['total_likes'] = stuff.total_likes()

        liked = False
        if stuff.likes.filter(pk = self.request.user.pk).exists():
            liked = True
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    context_object_name = "post"

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    context_object_name = "post"
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('detail_post', kwargs={'pk': self.kwargs['pk']})


class DeletePost(DeleteView):
    model = Post
    template_name = "delete_post.html"
    context_object_name = "post"
    success_url = reverse_lazy('home')

class CategoryList(ListView):
    model = Post
    # allow_empty = False
    context_object_name = "posts"
    template_name = "home.html"

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        active = get_object_or_404(Category, slug = self.kwargs['slug_id'])
        context['active'] = active.name
        if (context['posts'].count() > 0):
            context['title'] = context['posts'][0].category.name
        else:
            context['title'] =''
        return context
    
    def get_queryset(self, *args, **kwargs): #создание контекста
        return Post.objects.filter(category__slug = self.kwargs['slug_id'])

def LikeView(request, pk):

    post = get_object_or_404(Post, pk = request.POST.get('post_id'))

    if post.likes.filter(pk = request.user.id).exists():
        post.likes.remove(request.user.id) 
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('detail_post', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'add_comment.html'
    context_object_name = "post"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail_post', kwargs={'pk': self.kwargs['pk']})

    
class SearchView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("search"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("search")
        return context