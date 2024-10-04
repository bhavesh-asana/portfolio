# Generated by Django 5.1.1 on 2024-09-28 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarteq', '0003_remove_employeeparticulars_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='primaryAddress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primaryAddress', to='smarteq.address'),
        ),
    ]
