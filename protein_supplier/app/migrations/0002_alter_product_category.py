# Generated by Django 4.0.2 on 2022-02-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Milk'), ('V', 'Vegetables'), ('F', 'Fruits')], max_length=2),
        ),
    ]
