from django.db import models
from django.contrib.auth.models import User

class Aktiviteter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)

    class Meta:
        verbose_name = 'Aktiviteter'
        verbose_name_plural = 'Aktiviteter'



#blank og null means that we do not have to go back in the table to fill in the props.