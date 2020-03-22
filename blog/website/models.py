from django.db import models


class category(models.TextChoices):
    tech = 'TC', 'Technology'
    curiositys = 'CR', 'Curiositys'
    general = 'GR', 'General'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2, choices=category.choices, default=category.general,)
    delete = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title
