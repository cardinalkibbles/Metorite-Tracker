# Generated by Django 4.0.4 on 2022-06-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmic_event_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cosmicevent',
            old_name='year',
            new_name='date',
        ),
        migrations.AddField(
            model_name='cosmicevent',
            name='name',
            field=models.CharField(default='unnamed', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cosmicevent',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=500),
        ),
        migrations.AlterField(
            model_name='cosmicevent',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=500),
        ),
        migrations.AlterField(
            model_name='cosmicevent',
            name='mass',
            field=models.DecimalField(decimal_places=4, max_digits=500),
        ),
    ]