# Generated by Django 2.2.4 on 2020-10-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_employee_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]