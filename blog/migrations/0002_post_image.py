# Generated by Django 5.0.4 on 2024-05-14 06:19

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='posts'),
        ),
    ]
