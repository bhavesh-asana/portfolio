# Generated by Django 5.1.1 on 2024-09-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarteq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]