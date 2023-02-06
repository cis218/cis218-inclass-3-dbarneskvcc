from django.db import models

from django.urls import reverse


class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        """String method"""
        return self.title

    def get_absolute_url(self):
        """Get absolute URL of object"""
        return reverse(
            "post_detail",
            kwargs={"pk": self.pk},
        )
