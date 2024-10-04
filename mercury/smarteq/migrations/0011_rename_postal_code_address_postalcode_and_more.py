# Generated by Django 5.1.1 on 2024-09-29 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarteq', '0010_remove_employee_employeeparticulars_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='postal_code',
            new_name='postalCode',
        ),
        migrations.RemoveField(
            model_name='company',
            name='employeeParticulars',
        ),
        migrations.AddField(
            model_name='employeeparticulars',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smarteq.company'),
        ),
    ]