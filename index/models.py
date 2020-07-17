from django.db import models


class Post(models.Model):
    post = models.TextField()
    user = models.CharField(max_length = 127)
    img = models.URLField()

    def __str__(self):
        return self.post
