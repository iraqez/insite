from django.db import models
from tinymce.models import HTMLField

class Subdivision(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва підрозділу')
    slug = models.SlugField(verbose_name=r"Адресна строка", max_length=255, unique=True,
                           help_text='Унікальне значення в адресній строці, добавляється автоматично.')

    class Meta:
        verbose_name = u"Підрозділ"
        verbose_name_plural = u"Підрозділи"

    def __str__(self):
        return self.title

#Абстрактные классы

class Leading(models.Model):
    subdivision = models.ManyToManyField(Subdivision, verbose_name='Підрозділ')
    title = models.CharField(max_length=100, verbose_name='Назва')
    slug = models.SlugField(verbose_name=r"Адресна строка", max_length=255, unique=True,
                            help_text='Унікальне значення в адресній строці, добавляється автоматично.')
    text = HTMLField(verbose_name='Зміст')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Docs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва документу')
    file = models.FileField(verbose_name='Файл для скачування', upload_to='docs/')

    class Meta:
        abstract = True
        verbose_name = u"Документ"
        verbose_name_plural = u"Документи"

    def __str__(self):
        return self.title

#---------------------------------------------------------------------------------------------

class LeadingInstrukciy(Leading):
    class Meta:
        verbose_name = u"Інструкція"
        verbose_name_plural = u"Інструкції"

class LeadingPolozhennya(Leading):
    class Meta:
        verbose_name = u"Положення"
        verbose_name_plural = u"Положення"

class LeadingProcedure(Leading):
    class Meta:
        verbose_name = u"Процедура"
        verbose_name_plural = u"Процедури"

#---------------------------------------------------------------------------------------------------------
class DocsInstrukciy(Docs):
    leading = models.ForeignKey(LeadingInstrukciy, on_delete=models.CASCADE)

class DocsPolozhennya(Docs):
    leading = models.ForeignKey(LeadingPolozhennya, on_delete=models.CASCADE)

class DocsProcedure(Docs):
    leading = models.ForeignKey(LeadingProcedure, on_delete=models.CASCADE)