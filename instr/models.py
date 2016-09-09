from django.db import models

class Subdivision(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва підрозділу')

    class Meta:
        verbose_name = u"Підрозділ"
        verbose_name_plural = u"Підрозділи"

    def __str__(self):
        return self.title

class Leading(models.Model):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, verbose_name='Підрозділ')
    title = models.CharField(max_length=100, verbose_name='Назва процедури')
    text = models.TextField(verbose_name='Текст процедури')
    file = models.FileField(verbose_name='Файл для скачування')

    class Meta:
        verbose_name = u"Процедура"
        verbose_name_plural = u"Процедури"

    def __str__(self):
        return self.title
