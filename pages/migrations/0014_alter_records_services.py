# Generated by Django 4.1.13 on 2024-03-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_records_options_records_date_rec_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='services',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
