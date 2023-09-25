from django.db import models

# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='albums')
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name