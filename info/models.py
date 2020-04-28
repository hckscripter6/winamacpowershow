from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=120)
    content = RichTextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Info"
        
        
