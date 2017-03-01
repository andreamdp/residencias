# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppal', '0002_auto_20151006_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='residenciaaut',
            name='tipoInst',
            field=models.CharField(default=b'P', max_length=2, choices=[(b'U', b'P\xc3\xbablica'), (b'P', b'Privada')]),
        ),
    ]
