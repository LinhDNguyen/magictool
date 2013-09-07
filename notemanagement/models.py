from django.db import models

# Create your models here.
class Category(models.Model):
    """Category class"""

    name = models.CharField('name', max_length=200, unique=True, null=False, blank=False)
    desc = models.TextField('desc', blank=True, null=True)

    def __str__(self):
        return '%s' % self.name

    class Admin:
        pass

