from django.db import models

# Create your models here.


class Publication(models.Model):
    artwork = models.ImageField( default='blank.png', upload_to='upload/images', null=False, blank=True)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
