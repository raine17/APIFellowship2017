import os, sys, string, csv, datetime, time, django, pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "refugees.settings")

django.setup()

from reports.models import Country, State, City, RefugeeReport, StateCityCountry

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

reader = csv.reader(open("refugees0216-4.csv"), dialect=csv.excel)
next(reader)
for row in reader:

    refstate = row[0]
    refstate_slug = slugify(refstate)
    refstateid, refstateadded = State.objects.get_or_create(name=refstate, name_slug=refstate_slug)

    reforigin = row[3]
    reforigin_slug = slugify(reforigin)
    reforiginid, reforiginadded = Country.objects.get_or_create(name=reforigin, name_slug=reforigin_slug)

    popcity = row[5]
    popcity_slug = slugify(popcity)
    popcityid, popcityadded = City.objects.get_or_create(state=refstateid, name=popcity, name_slug=popcity_slug)

    cleanyear = row[1]
    cleanyear = cleanyear.replace('CY ', '')

    ref, refcreated = RefugeeReport.objects.get_or_create(country=reforiginid, state=refstateid, city=popcityid, year=cleanyear, city_total=row[6], state_total=row[2], country_total=row[4], all_countries=row[7])
    print(ref)

    scc, scccreated = StateCityCountry.objects.get_or_create(state=ref.state, city=ref.city, country=ref.country)
    print(scc)
