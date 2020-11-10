from django.db import models


class Counter(models.Model):
    count_number = models.IntegerField(verbose_name='Count number',
                                       default=5)
