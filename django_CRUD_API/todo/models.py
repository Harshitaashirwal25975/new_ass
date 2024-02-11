from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    no = models.IntegerField()
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


