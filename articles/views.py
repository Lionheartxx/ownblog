from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article, Comment
from .forms import CommentForm

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "summary", "body", "photo")
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # if user == superuser
    def test_func(self):
        return self.request.user.is_superuser

class ArticleCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('article_list')