from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
    source='image',
    processors=[Thumbnail(100,100)],
    format='JPEG',
    options={'quality': 90},
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    