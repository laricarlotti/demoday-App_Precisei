# Generated by Django 2.2.3 on 2019-09-25 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_login_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='login',
            name='sobrenome',
        ),
        migrations.RemoveField(
            model_name='login',
            name='usuario',
        ),
    ]