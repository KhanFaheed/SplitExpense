# Generated by Django 5.1.7 on 2025-03-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_item_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.FloatField(),
        ),
    ]
