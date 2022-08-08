# Generated by Django 4.0.6 on 2022-08-08 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=None, null=True, verbose_name='creation date')),
                ('modified_date', models.DateTimeField(default=None, null=True, verbose_name='modification date')),
                ('deleted_date', models.DateTimeField(default=None, null=True, verbose_name='delete date')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('category', models.CharField(default='NS', max_length=255, null=True, verbose_name='category')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='mail')),
                ('phone', models.IntegerField(verbose_name='phone')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCompany',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateTimeField(default=None, null=True, verbose_name='creation date')),
                ('modified_date', models.DateTimeField(default=None, null=True, verbose_name='modification date')),
                ('deleted_date', models.DateTimeField(default=None, null=True, verbose_name='delete date')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('category', models.CharField(default='NS', max_length=255, null=True, verbose_name='category')),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='mail')),
                ('phone', models.IntegerField(verbose_name='phone')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Company',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
