# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad_A', models.PositiveIntegerField(verbose_name=b'cantidad de A\xc3\xb1os')),
                ('tipo', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
                ('director', models.CharField(max_length=50)),
                ('secretaria', models.CharField(max_length=50)),
                ('telefonos', models.CharField(max_length=50)),
                ('OtrosContactos', models.TextField(verbose_name=b'Otros Contactos', blank=True)),
            ],
            options={
                'verbose_name': 'Instituci\xf3n',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='ResidenciaAut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expediente', models.CharField(default=b'0-0-00', max_length=12, blank=True, help_text=b'####-####/##', null=True, verbose_name=b'N\xc2\xb0 de Expediente del Ministerio de Salud')),
                ('a_Comienzo', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1o')),
                ('cantA_1', models.PositiveSmallIntegerField(verbose_name=b'1er. A\xc3\xb1o')),
                ('cantA_2', models.PositiveSmallIntegerField(verbose_name=b'2do. A\xc3\xb1o')),
                ('cantA_3', models.PositiveSmallIntegerField(verbose_name=b'3er. A\xc3\xb1o')),
                ('cantA_4', models.PositiveSmallIntegerField(verbose_name=b'4to. A\xc3\xb1o')),
                ('jefeResidentes', models.PositiveSmallIntegerField(verbose_name=b'Jefe de Residentes')),
                ('fechaEvaluacColMed', models.DateField(verbose_name=b'Fecha de Evaluaci\xc3\xb3n', blank=True)),
                ('fechaEvaluacMixta', models.DateField(null=True, verbose_name=b'Fecha de Evaluaci\xc3\xb3n Mixta', blank=True)),
                ('fechaCeseActividad', models.DateField(null=True, verbose_name=b'Fecha de Vencimiento Acreditaci\xc3\xb3n', blank=True)),
                ('jefeServicio', models.CharField(max_length=50, null=True, verbose_name=b'Jefe de Servicio', blank=True)),
                ('coordinador', models.CharField(max_length=50, null=True, verbose_name=b'Coordinador', blank=True)),
                ('asesorDocente', models.CharField(max_length=150, verbose_name=b'Asesor Docente', blank=True)),
                ('tipo', models.CharField(blank=True, max_length=2, choices=[(b'C', b'Colegio'), (b'M', b'Mixta')])),
                ('memo', models.TextField(null=True, verbose_name=b'memo', blank=True)),
                ('especialidad', models.ForeignKey(related_name='+', blank=True, to='ppal.Especialidad', null=True)),
                ('institucion', models.ForeignKey(related_name='+', blank=True, to='ppal.Institucion', null=True)),
            ],
            options={
                'verbose_name': 'Residencia',
                'verbose_name_plural': 'Residencias',
            },
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('tipoR', models.IntegerField()),
                ('residencia', models.ForeignKey(related_name='+', to='ppal.ResidenciaAut')),
            ],
        ),
        migrations.AddField(
            model_name='institucion',
            name='localidad',
            field=models.ForeignKey(to='ppal.Localidad'),
        ),
    ]
