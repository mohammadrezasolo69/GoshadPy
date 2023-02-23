{%- if cookiecutter.use_jalali == 'y' -%}
from django_jalali.db import models as jmodels
{%- endif -%}

from django.db import models
from django.utils.translation import gettext_lazy as _

class DateBasic(models.Model):
    class Meta:
        abstract = True

    {%- if cookiecutter.use_jalali == 'y' -%}
    created_at_jalali = jmodels.jDateTimeField(_('created at'), auto_now_add=True)
    updated_at_jalali = jmodels.jDateTimeField(_('updated at'), auto_now=True)

    def get_created_at_jalali(self):
        return self.created_at_jalali.strftime('%H:%M - %Y/%m/%d')

    def get_updated_at_jalali(self):
        return self.updated_at_jalali.strftime('%H:%M - %Y/%m/%d')
    {%- endif -%}

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)


    def get_created_at(self):
        return self.created_at.strftime('%H:%M - %Y/%m/%d')
    def get_updated_at(self):
        return self.updated_at.strftime('%H:%M - %Y/%m/%d')
