from django.db import models
from django.contrib.auth.models import (UserManager, AbstractBaseUser, PermissionsMixin)

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Please provide a valid email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    profile_pic = models.ImageField( default='nuser.png', upload_to='upload/profile', null=True, blank=True)
    email = models.CharField(max_length=50, null=False,
                             blank=False, unique=True,)
    name = models.CharField(max_length=50, null=False,
                            blank=False, unique=True)
    
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateField(blank=True, null=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def get_full_name(self):
        return self.name


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
   
       


       