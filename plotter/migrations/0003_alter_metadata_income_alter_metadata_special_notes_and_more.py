# Generated by Django 4.0.3 on 2022-04-20 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0002_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='income',
            field=models.CharField(blank=True, db_column='IncomeGroup', max_length=150, null=True, verbose_name='IncomeGroup'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='special_notes',
            field=models.CharField(blank=True, db_column='SpecialNotes', max_length=940, null=True, verbose_name='SpecialNotes'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='table_name',
            field=models.CharField(blank=True, db_column='TableName', max_length=150, null=True, verbose_name='TableName'),
        ),
        migrations.AlterModelTable(
            name='metadata',
            table='MetadataCountries',
        ),
    ]
