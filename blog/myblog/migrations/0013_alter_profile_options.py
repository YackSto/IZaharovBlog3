# Generated by Django 3.2.8 on 2021-11-16 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user'], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
