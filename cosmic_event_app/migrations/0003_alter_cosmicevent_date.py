# Generated by Django 4.0.5 on 2022-06-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmic_event_app', '0002_rename_year_cosmicevent_date_cosmicevent_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosmicevent',
            name='date',
            field=models.DateField(),
        ),
    ]
