from django.contrib import admin

# Register your models here.
from .models import Country, State, City, RefugeeReport

class CityAdmin(admin.ModelAdmin):
    list_filter = ('state',)

admin.site.register(Country)

admin.site.register(State)

admin.site.register(City, CityAdmin)

admin.site.register(RefugeeReport)
