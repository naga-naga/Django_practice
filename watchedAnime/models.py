from django.db import models

# Create your models here.
class Anime(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=255)
    year = models.IntegerField(verbose_name="放送年", blank=True, null=True)
    updated_date = models.DateField(verbose_name="登録日", auto_now=True)

    def __str__(self):
        return self.title