import os, sys, string, csv, datetime, time, django, pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "refugees.settings")

django.setup()

from refugees.models import Country, State, City, StateCount, StateCountTotal, CityCount, CountryCount, RefugeeReport

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

reader = csv.reader(open("downloads/refugees2016.csv"), dialect=csv.excel)
next(reader)
for row in reader:

    refstate = row[0]
    refstate_slug = slugify(refstate)
    stateid, stateadded = ResettledState.objects.get_or_create(name=refstate, name_slug=refstate_slug)

    refyear = row[1]
    refyear_slug = slugify(refyear)
    refyearid, refyearadded = Year.objects.get_or_create(name=refyear, name_slug=refyear_slug)

    statetotal = row[2]
    statetotal_slug = slugify(statetotal)
    statetotalid, statetotaladded = TotalResettledState.objects.get_or_create(name=StateCount, name_slug=statetotal_slug)

    reforigin = row[3]
    reforigin_slug = slugify(reforigin)
    reforiginid, reforiginadded = RefugeeOrigin.objects.get_or_create(name=reforigin, name_slug=reforigin_slug)

    popstate = row[4]
    popstate_slug = slugify(popstate)
    popstateid, popstateadded = RefugeesResettledState.objects.get_or_create(name=RefugeesResettledState, name_slug)

    refcity = row[5]
    refcity_slug = slugify(refcity)
    cityid, cityadded = ResettledCity.objects.get_or_create(name=refcity, name_slug=refcity_slug)

    popcity =row[8]
    popcity_slug = slugify (popcity)
    popcityid, popcityadded = RefugeesResettledCity.objects.get_or_create(name=popcity, name_slug=popcity_slug)

    popcountry = row[9]
    popcountry_slug = slugify (popcountry)
    popcountryid, popcountryadded = RefugeesResettledUS.objects.get_or_create(name=popcountry, name_slug=popcountry_slug)

    ref = RefugeeReport(ResettledState=refstate, Year=refyear, TotalResettledState=statetotal, RefugeeOrigin=reforigin, RefugeesResettledState=popstate, ResettledCity=refcity, RefugeesResettledCity=popcity, RefugeesResettledUS=popcountry)
    print(ref)
    ref.save()
