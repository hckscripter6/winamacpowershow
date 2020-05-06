from django.db import models

# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='Tractor Show', null=True)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name