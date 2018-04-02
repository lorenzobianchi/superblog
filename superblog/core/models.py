from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', null=True, blank=True)
    author_photo = models.ImageField(blank=True, null=True, upload_to='images/')
    main_photo = models.ImageField(blank=True, null=True, upload_to='images/')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now, blank=True, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    
