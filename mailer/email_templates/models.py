from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractEmailTemplate(models.Model):
    slug = models.SlugField(max_length=100, null=False, blank=False, unique=True, verbose_name=_('Slug'))
    subject = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Subject'))
    html_body = models.TextField(null=False, blank=False, verbose_name=_('HTML body'))

    class Meta:
        abstract = True
        verbose_name = _('E-mail')
        verbose_name_plural = _('E-mails')


class EmailTemplate(AbstractEmailTemplate):
    pass
