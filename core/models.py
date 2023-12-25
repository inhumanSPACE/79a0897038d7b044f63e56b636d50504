from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe


class Function(models.Model):
    statement = models.CharField(max_length=128, verbose_name='Функция')
    dt = models.IntegerField(verbose_name='Шаг t, часы')
    interval = models.IntegerField(verbose_name='Интервал t, дней')
    graph = models.ImageField(null=True, blank=True, upload_to='media/', verbose_name='График')
    creation_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата обработки')

    def __str__(self):
        return self.statement

    class Meta:
        verbose_name = _('функцию')
        verbose_name_plural = _('функции')

    def save(self, *args, **kwargs):
        super(Function, self).save(*args, **kwargs)
        if not args:
            from .tasks import generate_picture
            generate_picture.delay(self.id)

    def image_tag(self):
        return mark_safe(f'<img src="/media/{self.graph}" width="300" height="300" />')

    image_tag.short_description = 'Image'
