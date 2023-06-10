from django.db import models

# Create your models here.


class Travel(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    img = models.ImageField(upload_to='pics')
    name1 = models.CharField(max_length=250)
    pos = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name1

