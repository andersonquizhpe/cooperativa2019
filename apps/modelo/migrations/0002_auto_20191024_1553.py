# Generated by Django 2.2.6 on 2019-10-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadocivil',
            field=models.CharField(choices=[('s', 'soltero'), ('c', 'casado'), ('d', 'divorciado'), ('v', 'viudo')], default='soltero', max_length=20),
        ),
    ]