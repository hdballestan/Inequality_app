from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from plotter.models import Data, Metadata
from import_export import resources


class CategoricalResources(resources.ModelResource):
    class Meta:
        model = Metadata


class CategoricalResources2(resources.ModelResource):
    class Meta:
        model = Data


class DataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("country_name", "si", "siu", "sid")
    list_filter = ("country_name",)


admin.site.register(Data, DataAdmin)


class MetadataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("region", "income")
    list_filter = ("region",)


admin.site.register(Metadata, MetadataAdmin)

# Register your models here.
