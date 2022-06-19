from django.contrib import admin
from .models import Diagnoses, ParametersList, Parameters


admin.site.register(Diagnoses)
admin.site.register(ParametersList)
admin.site.register(Parameters)
