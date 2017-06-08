import os, sys, string, csv, datetime, time, django, pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "refugees.settings")

django.setup()

from refugees.models import Country, State, City, RefugeeReport

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

reader = csv.reader(open("downloads/refugees2016.csv"), dialect=csv.excel)
next(reader)
for row in reader:

    refstate = row[0]
    refstate_slug = slugify(refstate)
    stateid, stateadded = State.objects.get_or_create(name=refstate, name_slug=refstate_slug)

    refyear = row[1]
    refyear_slug = slugify(refyear)
    refyearid, refyearadded = Year.objects.get_or_create(name=refyear, name_slug=refyear_slug)

    reforigin = row[3]
    reforigin_slug = slugify(reforigin)
    reforiginid, reforiginadded = Country.objects.get_or_create(name=reforigin, name_slug=reforigin_slug)

    popcity =row[6]
    popcity_slug = slugify (popcity)
    popcityid, popcityadded = City.objects.get_or_create(name=popcity, name_slug=popcity_slug)

    ref = RefugeeReport(State=refstate, Year=refyear, Country=reforigin, City=popcity)
    print(ref)
    ref.save()
