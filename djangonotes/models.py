from django.db import models


class Note(models.Model):
    text = models.TextField()
    unique_words = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.text
