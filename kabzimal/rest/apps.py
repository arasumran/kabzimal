from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class KabzimalRestConfig(AppConfig):
    name = 'kabzimal.rest'
    label = 'kabzimal_rest'
    verbose_name = _('Kabzimal Rest')

