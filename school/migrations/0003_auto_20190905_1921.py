# Generated by Django 2.1.1 on 2019-09-05 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190905_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['group'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]
