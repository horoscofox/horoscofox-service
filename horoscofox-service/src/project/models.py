from django.db import models
from enum import Enum
from horoscofox.constants import SIGNS

SIGNS_CHOICES = (
    (0, 'capricorn'),
    (1, 'acquarius'),
    (2, 'pisces'),
    (3, 'aries'),
    (4, 'taurus'),
    (5, 'gemini'),
    (6, 'cancer'),
    (7, 'leo'),
    (8, 'virgo'),
    (9, 'libra'),
    (10, 'scorpio'),
    (11, 'sagittarius')
)

KINDS_CHOICES = (
    (1, ("today")),
    (2, ("tomorrow")),
    (3, ("month")),
    (4, ("info"))
)


class Horoscope(models.Model):
    text = models.TextField()
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    sign = models.IntegerField(choices=SIGNS_CHOICES, default=1)
    kind = models.IntegerField(choices=KINDS_CHOICES, default=1)

    @classmethod
    def get_sign_key(cls, sign: str):
        for key, value in SIGNS_CHOICES:
            if sign == value:
                return key
