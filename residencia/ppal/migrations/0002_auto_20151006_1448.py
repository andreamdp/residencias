# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='residenciaaut',
            name='instructor',
            field=models.CharField(max_length=150, verbose_name=b'Instructor de Residentes', blank=True),
        ),
        migrations.AddField(
            model_name='residenciaaut',
            name='jefedocencia',
            field=models.CharField(max_length=150, verbose_name=b'Jefe Docencia', blank=True),
        ),
    ]
