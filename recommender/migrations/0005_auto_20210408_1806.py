# Generated by Django 3.1.7 on 2021-04-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0004_auto_20210408_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='outcome',
            field=models.CharField(max_length=8),
        ),
    ]
