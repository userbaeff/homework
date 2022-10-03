from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=30)
    post_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.post_name}'


class Comment(models.Model):
    username = models.CharField(max_length=15)
    comment = models.TextField()

    def __str__(self):
        return f'{self.username} \n {self.comment}'
