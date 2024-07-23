# Generated by Django 5.0.7 on 2024-07-22 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='dep_name',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep_names', to='schoolsystem.departmentmodel'),
        ),
    ]
