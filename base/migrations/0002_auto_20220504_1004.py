# Generated by Django 3.2 on 2022-05-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='education',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='level',
            name='levels',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagelist',
            name='page',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]