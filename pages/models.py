from django.db import models
from datetime import datetime

class Page(models.Model):
    product_1_photo = models.ImageField(upload_to='photos/pages/%Y/%m/%d/')
    product_1_description = models.TextField()
    product_2_photo = models.ImageField(upload_to='photos/pages/%Y/%m/%d/')
    product_2_description = models.TextField()
    product_3_photo = models.ImageField(upload_to='photos/pages/%Y/%m/%d/')
    product_3_description = models.TextField()
    quality_content = models.TextField()
    services_content = models.TextField()
    on_time_content = models.TextField()
    about_heading = models.TextField()
    about_content_1 = models.TextField()
    about_photo = models.ImageField(upload_to='photos/pages/%Y/%m/%d/')
    about_content_2 = models.TextField()
    product_support_photo = models.ImageField(upload_to='photos/pages/%Y/%m/%d/')
    product_support_number = models.CharField(max_length=20)
    product_support_mail = models.CharField(max_length=50)
    list_date = models.DateTimeField(default=datetime.now,)
