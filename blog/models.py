from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    date_published = models.DateTimeField(default = timezone.now)
    date_updated = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})