# Generated by Django 4.0.6 on 2022-08-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_employee_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary_per_hour',
            field=models.FloatField(default=None, max_length=255, null=True, verbose_name='salary'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='salary_per_hour',
            field=models.FloatField(default=None, max_length=255, null=True, verbose_name='salary'),
        ),
    ]
