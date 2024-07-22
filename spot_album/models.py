from django.db import models

# Create your models here.


class Publication(models.Model):
    text = models.TextField()
    artwork = models.ImageField( default='blank.png', upload_to='upload/images', null=False, blank=True)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.id)

class Comments(models.Model):
    comment_text =models.TextField()
    comment_artwork = models.ImageField( default='blank.png', upload_to='upload/images', null=True, blank=True)
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE)
    
    