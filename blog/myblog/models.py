from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name = "Заголовок")
    snippet = models.CharField(max_length=255, verbose_name = "Превью", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Автор", )
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории", null=True, blank = True)
    body = RichTextField(max_length=255, blank=True, null=True, verbose_name = "Содержимое")
    # body = models.TextField(verbose_name="Содержимое")
    photo = models.ImageField(upload_to="blogs/", verbose_name="Фотография", null=True, blank = True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    likes = models.ManyToManyField(User, related_name="blog_post")
    
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"{self.title} - {str(self.author)}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-time_created']
    
    def get_absolute_url(self):
        return reverse('detail_post', args=(str(self.id))) #корректная работа формы POST

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, verbose_name = "Биография")
    profile_pic = models.ImageField(blank=True, verbose_name = "Аватар", null=True, upload_to ="avatars/")
    title = models.CharField(max_length=255, verbose_name = "Заголовок", null=True, blank = True)
    website_url = models.CharField(max_length=255, verbose_name = "Личный сайт", null=True, blank = True)
    fb_url = models.CharField(max_length=255, verbose_name = "Facebook", null=True, blank = True)
    twitter_url = models.CharField(max_length=255, verbose_name = "Twitter", null=True, blank = True)
    instagram_url = models.CharField(max_length=255, verbose_name = "Instagram", null=True, blank = True)
    vk_url = models.CharField(max_length=255, verbose_name = "Вконтакте", null=True, blank = True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ['user']

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, verbose_name = "URL")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["time_created"]
