from imagekit.processors import Thumbnail, ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField
from django.db import models

# Create your models here.

class Movie(models.Model):
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnalis/',
        processors=[Thumbnail(200,200)],
        format='JPEG',
        options={'quality': 90},
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(100,100)],
        format='JPEG',
        options={'quality': 90},
    )
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    synopsis = models.TextField()
    