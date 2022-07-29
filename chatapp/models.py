from django.db import models

# Create your models here.
class Bericht(models.Model):
    inhoud = models.CharField(max_length=255)
    verzender = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Berichten'