from django.contrib import admin
from Incidents.models import *
from Subdivisions.models import *
# Register your models here.
admin.site.register(Incidents)
admin.site.register(Specifications)
admin.site.register(Subdivisions)
