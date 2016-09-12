from django.db import models
from tinymce.models import HTMLField

class Subdivision(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва підрозділу')

    class Meta:
        verbose_name = u"Підрозділ"
        verbose_name_plural = u"Підрозділи"

    def __str__(self):
        return self.title


class Leading(models.Model):
    subdivision = models.ManyToManyField(Subdivision, verbose_name='Підрозділ')
    title = models.CharField(max_length=100, verbose_name='Назва процедури')
    text = HTMLField(verbose_name='Зміст процедури')

    class Meta:
        verbose_name = u"Процедура"
        verbose_name_plural = u"Процедури"

    def __str__(self):
        return self.title

class Docs(models.Model):
    leading = models.ForeignKey(Leading, on_delete=models.CASCADE)
    file = models.FileField(verbose_name='Файл для скачування')

    class Meta:
        verbose_name = u"Документ"
        verbose_name_plural = u"Документи"

