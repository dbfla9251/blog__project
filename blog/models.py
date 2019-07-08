from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('data published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text