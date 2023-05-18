from django.db import models
from django.utils import timezone

# Create your models here.


CATEGORY_CHOICES = (
    ('WD','Web Development'),
    ('MD','Mobile Development'),
    ('DS','Data Science'),
    
)





class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    email = models.EmailField( max_length=254, null=True,blank=True )
    views_count = models.IntegerField(default=0)
    category = models.CharField(choices= CATEGORY_CHOICES,max_length=20)
    
    def __str__(self):
        return self.title
