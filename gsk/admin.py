from django.contrib import admin
from gsk.models import Garage


# class GarageAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Garage

admin.site.register(Garage)