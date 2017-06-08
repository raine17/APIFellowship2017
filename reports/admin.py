from django.contrib import admin

# Register your models here.
from .models import Country, State, City, RefugeeReport

admin.site.register(Country)

admin.site.register(State)

admin.site.register(City)

admin.site.register(RefugeeReport)
