# Generated by Django 5.1.1 on 2024-09-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarteq', '0006_remove_employeeparticulars_employmentauthorization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentauthorization',
            name='cardNumber',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='employmentauthorization',
            name='uscisNumber',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
