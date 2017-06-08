from django.shortcuts import render

from reports.models import Country, State, City, RefugeeReport

def home(request):
    context = {}
    return render(request, 'index.html', context)

def state_list(request):
    states = State.objects.order_by('name')
    context = {'states': states}
    return render(request, 'state_list.html', context)

def city_list(request, state_slug):
    state = State.objects.get(name_slug=state_slug)
    cities = City.objects.filter(state__name_slug=state_slug)
    context = {'state': state, 'cities': cities}
    return render(request, 'city_list.html', context)

def country_list(request, state_slug, city_slug):
    state = State.objects.get(name_slug=state_slug)
    city = City.objects.get(name_slug=city_slug)
    countries = Country.objects.filter(city=city)
    context = {'state': state, 'city': city, 'countries': countries}
    return render(request, 'country_list.html', context)

def country_detail(request, state_slug, city_slug, country_slug):
    state = State.objects.get(name_slug=state_slug)
    city = City.objects.get(name_slug=city_slug)
    country = Country.objects.get(name_slug=country_slug)
    reports = RefugeeReport.objects.filter(country=country, city=city).order_by('year')
    context = {'state': state, 'city': city, 'country': country, 'reports': reports}
    return render(request, 'country_detail.html', context)
