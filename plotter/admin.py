from django.contrib import admin
from plotter.models import Data, Metadata


class DataAdmin(admin.ModelAdmin):
    pass
admin.site.register(Data, DataAdmin)


class MetadataAdmin(admin.ModelAdmin):
    pass
admin.site.register(Metadata, MetadataAdmin)

# Register your models here.
