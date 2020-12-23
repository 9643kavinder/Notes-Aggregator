from django.db import models


class NotePost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=5000, null=False, blank=False)

    def __str__(self):
        return self.title