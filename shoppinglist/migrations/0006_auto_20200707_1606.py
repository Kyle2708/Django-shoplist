# Generated by Django 3.0.8 on 2020-07-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0005_auto_20200707_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathtest',
            name='path',
            field=models.URLField(),
        ),
    ]
