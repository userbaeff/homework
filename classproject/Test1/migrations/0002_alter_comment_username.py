# Generated by Django 4.1.1 on 2022-10-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=15),
        ),
    ]
