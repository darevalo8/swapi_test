# Generated by Django 2.2.13 on 2021-07-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210710_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green'), ('purlple', 'Purlple'), ('unknown', 'Unknown'), ('n/a', 'N/A')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='skin_color',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]