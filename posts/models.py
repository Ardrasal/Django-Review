from django.db import models
from datetime import datetime

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    """
    Changes name of Post in admin from 'object post 1' to title of post.
    """
    def __str__(self):
        return self.title
        
    class Meta:
        """
        Changes Postss in admin to Posts.
        """
        verbose_name_plural = "Posts"
