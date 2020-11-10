# Generated by Django 3.1.3 on 2020-11-10 02:54

from django.db import migrations


def init_data(apps, schema_editor):
    """
    Add a new record as default to the Counter table.
    """
    counter = apps.get_model('api', 'Counter')
    record, created = counter.objects.get_or_create(count_number=5)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_data),
    ]