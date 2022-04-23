from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.core.validators import MaxLengthValidator
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(validators=[MaxLengthValidator(100)], blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.article.title, self.name)
    
    def get_absolute_url(self):
        return reverse('article_list')
    class Meta():
        ordering = ['-date_added']