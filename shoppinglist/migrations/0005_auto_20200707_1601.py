# Generated by Django 3.0.8 on 2020-07-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0004_imagetest'),
    ]

    operations = [
        migrations.CreateModel(
            name='pathtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('path', models.FilePathField()),
            ],
        ),
        migrations.AlterField(
            model_name='imagetest',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]