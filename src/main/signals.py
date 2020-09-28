import re

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    instance.phone = re.sub(r'\D', '', instance.phone)
