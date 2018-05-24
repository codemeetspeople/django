from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        verbose_name=_('Название')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ('id',)


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        verbose_name=_('Название')
    )
    content = models.TextField(
        null=False,
        verbose_name=_('Контент')
    )
    category_id = models.ForeignKey(
        to='Category',
        null=False,
        on_delete='DO_NOTHING',
        verbose_name=_('Категория')
    )
    image = models.ImageField(
        verbose_name=_('Изображение'),
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')
