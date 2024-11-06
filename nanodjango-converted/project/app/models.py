from django.db import models


class Comment(models.Model):
    """
    Comments model
    """

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
