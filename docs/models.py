from django.db import models
from tinymce.models import HTMLField

class Subdivision(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва підрозділу')
    slug = models.SlugField(verbose_name=r"Адресна строка", max_length=255, unique=True,
                           help_text='Унікальне значення в адресній строці, добавляється автоматично.')

    class Meta:
        verbose_name = u"Підрозділ"
        verbose_name_plural = u"Підрозділи"
        ordering = [ 'title', ]

    def __str__(self):
        return self.title

class Leading(models.Model):
    DOC_TYPE_CHOICES = (
        ('INSTR', 'Інструкція'),
        ('POL', 'Положення'),
        ('PROC', 'Процедура'),

    )
    doc_type_choices = models.CharField(max_length=5,
                                      choices=DOC_TYPE_CHOICES,
                                      default='INSTR',verbose_name='Тип документу', help_text='Оберіть тип документу(інструкція, положення, процедура)')
    subdivision = models.ManyToManyField(Subdivision, verbose_name='Підрозділ')
    title = models.CharField(max_length=100, verbose_name='Назва')
    slug = models.SlugField(verbose_name=r"Адресна строка", max_length=255, unique=True,
                            help_text='Унікальне значення в адресній строці, добавляється автоматично.')
    text = HTMLField(verbose_name='Зміст')

    class Meta:
        verbose_name = u"Документ"
        verbose_name_plural = u"Документи"
        ordering = ['title',]

    class GetDoc()

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

class DocsLeading(Docs):
    leading = models.ForeignKey(Leading, on_delete=models.CASCADE)
