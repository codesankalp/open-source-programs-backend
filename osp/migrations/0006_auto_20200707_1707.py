# Generated by Django 3.0.6 on 2020-07-07 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osp', '0005_auto_20200625_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='form',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
    ]