from django.contrib import admin

# Register your models here.
from .models import Country, State, City, StateCount, StateCountTotal, CityCount, CountryCount, RefugeeReport

admin.site.register(Country)

admin.site.register(State)

admin.site.register(City)

admin.site.register(StateCount)

admin.site.register(StateCountTotal)

admin.site.register(CityCount)

admin.site.register(CountryCount)

admin.site.register(RefugeeReport)
