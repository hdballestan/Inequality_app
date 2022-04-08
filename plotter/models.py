from django.db import models


class BaseMeta(models.Model):
    country_code = models.CharField(max_length=3, verbose_name='Country Code', null=True, blank=True,
                                    db_column='Country Code')
    region = models.CharField(max_length=150, verbose_name='Region', null=True, blank=True, db_column='Region')
    income = models.CharField(max_length=150, verbose_name='Income Group', null=True, blank=True,
                              db_column='Income Group')
    special_notes = models.CharField(max_length=150, verbose_name='Special Notes', null=True, blank=True,
                                     db_column='Special Notes')
    table_name = models.CharField(max_length=150, verbose_name='Table Name', null=True, blank=True,
                                  db_column='Table Name')

    class Meta:
        abstract = True


class Metadata(BaseMeta):
    class Meta:
        db_table = "Metadata-Countries"
        verbose_name = 'country'
        verbose_name_plural = 'countries'
