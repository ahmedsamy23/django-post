from django.db import models

# Create your models here.

class About(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us/images/')
    
    def __str__(self):
        return self.title