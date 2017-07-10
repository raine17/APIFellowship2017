from django.shortcuts import render
from reports.models import Country, State, City, RefugeeReport
from django.db.models import Sum

def index(request):
    cities = City.objects.order_by('name')
    context = {'cities': cities}
    return render(request, 'index.html', context)

def resources_page(request):
    return render(request, 'resources_page.html', {})

def background_info(request):
    return render(request, 'background_info.html', {})

def about(request):
    return render(request, 'about.html', {})

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
    city = City.objects.get(name_slug=city_slug, state__name_slug=state_slug)
    countries = RefugeeReport.objects.filter(city=city)

    all_refugee_total = RefugeeReport.objects.filter(city=city).aggregate(Sum('city_total'))
    country_totals = RefugeeReport.objects.filter(city=city).values('country__name').annotate(total=Sum('city_total')).order_by('-total')
    context = {'country_totals': country_totals, 'all_refugee_total': all_refugee_total, 'state': state, 'city': city, 'countries': countries}

    return render(request, 'country_list.html', context)

def country_detail(request, state_slug, city_slug, country_slug):
    state = State.objects.get(name_slug=state_slug)
    city = City.objects.get(name_slug=city_slug)
    country = Country.objects.get(name_slug=country_slug)
    reports = RefugeeReport.objects.filter(country=country, city=city).order_by('year')
    context = {'state': state, 'city': city, 'country': country, 'reports': reports}
    return render(request, 'country_detail.html', context)
