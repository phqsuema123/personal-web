from django.db import models

# Create your models here.
# adminpanel/models.py

from django.db import models

class HomepageContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    body = models.TextField()
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
