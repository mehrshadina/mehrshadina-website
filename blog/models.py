from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True)
    images = models.ManyToManyField('Image', blank=True)
    content = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    time_required = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='img/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Image, self).delete(*args, **kwargs)
