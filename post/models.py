from django.db import models
from django.forms import CharField
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """Model definition for Post."""

    # Define fields here
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post-image/' , null=True , blank=True)
    active = models.BooleanField(default=False)
    category = models.ForeignKey("Category" , on_delete=models.CASCADE , null=True , blank=True)
    
    slug = models.SlugField(blank=True , null=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title) # slugify :  تحويل النص الى نص مفهرس
        super(Post , self).save(*args , **kwargs)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class CommentPost(models.Model):
    """Model definition for CommentPost."""

    # Define fields here

    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comment_post' , null=True , blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for CommentPost."""

        verbose_name = 'CommentPost'
        verbose_name_plural = 'CommentPosts'

    def __str__(self):
        """Unicode representation of CommentPost."""
        return f'{self.post.title} - {self.comment}'
