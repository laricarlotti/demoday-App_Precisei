# Generated by Django 2.2.6 on 2019-10-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190927_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True, verbose_name='Email'),
        ),
    ]
