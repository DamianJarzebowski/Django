# Generated by Django 4.2 on 2024-01-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://canape.cdnflexcatering.com/themes/frontend/default/images/img-placeholder.png', max_length=500),
        ),
    ]
