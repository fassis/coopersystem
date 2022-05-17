from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_interval(value):
    if value < 0.0:
        raise ValidationError(
            _('%(value)s deve ser maior que zero'), 
            params={'value': value},
            )

def validate_situation(value):
    from core.models import ENTREGUE, ENVIADO, PENDENTE
    if value not in [PENDENTE,ENVIADO,ENTREGUE]:
        raise ValidationError(
            _('%(value)s status de pedido inválido'), 
            params={'value': value},
            )