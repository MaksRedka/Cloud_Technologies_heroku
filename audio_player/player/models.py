from django.db import models


class Audio(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
        