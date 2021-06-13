from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    stars = models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=120)

    def _str_(self):
        return self.title