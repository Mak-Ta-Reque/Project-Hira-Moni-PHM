from django.db import models
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=200)
    violance = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.violance)
