from django.db import models

# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    text = models.TextField()
    artwork = models.ImageField( default='blank.png', upload_to='upload/images', null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

class Comments(models.Model):
    comment_text =models.TextField()
    comment_artwork = models.ImageField( default='blank.png', upload_to='upload/images', null=True, blank=True)
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comments_date = models.DateField(auto_now_add=True)
   
       
    

       