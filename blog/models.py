from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.create_at}"

# Create your models here.
