from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    display_pic = models.ImageField(default='gallery1.png', null=True, blank=True)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title
    