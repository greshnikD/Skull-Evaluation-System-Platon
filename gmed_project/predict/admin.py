from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import DotList, Coordinates, DotPairs


class DotListAdmin(ModelAdmin):
    list_display = ['name', 'description', 'computability']


class DotPairsAdmin(ModelAdmin):
    list_display = ['dot_1', 'dot_2']


admin.site.register(DotList, DotListAdmin)
admin.site.register(DotPairs, DotPairsAdmin)
admin.site.register(Coordinates)
