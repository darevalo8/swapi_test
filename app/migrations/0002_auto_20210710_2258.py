# Generated by Django 2.2.13 on 2021-07-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('blonde', 'Blonde'), ('red', 'Red'), ('white', 'White'), ('bald', 'Bald'), ('unknown', 'Unknown'), ('n/a', 'N/A')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='skin_color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green'), ('purlple', 'Purlple'), ('unknown', 'Unknown'), ('n/a', 'N/A')], max_length=32),
        ),
    ]
