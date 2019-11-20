from django.db import models
from datetime import datetime

class Client(models.Model):
    title = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/bags/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
