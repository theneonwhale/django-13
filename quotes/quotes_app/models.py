from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    quote = models.CharField(max_length=1500)
    tags = models.ManyToManyField(Tag, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.user.username}({self.user.email}): {self.quote} - {self.author.fullname}'
