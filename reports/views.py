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

def stories(request):
    return render(request, 'stories.html', {})

def state_list(request):
    state = State.objects.order_by('name')
    context = {'state': state}
    return render(request, 'state_list.html', context)

def city_list(request, state_slug):
    state = State.objects.get(name_slug=state_slug)
    state_totals = RefugeeReport.objects.filter(state=state).values('year').annotate(total=Sum('city_total')).order_by('year')
    cities = City.objects.filter(state__name_slug=state_slug).order_by('name')
    count_cities = len(cities)
    statewide_sum = RefugeeReport.objects.filter(state=state).aggregate(total=Sum('city_total'))
    context = {'state': state, 'cities': cities, 'state_totals': state_totals, 'count_cities' : count_cities, 'statewide_sum' : statewide_sum}
    return render(request, 'city_list.html', context)

def country_list(request, state_slug, city_slug):
    state = State.objects.get(name_slug=state_slug)
    city = City.objects.get(name_slug=city_slug, state__name_slug=state_slug)
    countries = RefugeeReport.objects.filter(city=city)
    city_by_year = RefugeeReport.objects.filter(city=city).values('year').annotate(total=Sum('city_total')).order_by('year')
    all_refugee_total = RefugeeReport.objects.filter(city=city).aggregate(Sum('city_total'))
    country_totals = Country.objects.filter(refugeereport__city=city).annotate(total=Sum('refugeereport__city_total')).order_by('-total')
    context = {'country_totals': country_totals, 'all_refugee_total': all_refugee_total, 'state': state, 'city': city, 'countries': countries, 'city_by_year': city_by_year}
    return render(request, 'country_list.html', context)

def country_detail(request, state_slug, city_slug, country_slug):
    state = State.objects.get(name_slug=state_slug)
    country = Country.objects.get(name_slug=country_slug)
    city = City.objects.get(name_slug=city_slug, state__name_slug=state_slug)
    city_by_year = RefugeeReport.objects.filter(city=city).values('year').annotate(total=Sum('city_total')).order_by('year')
    all_refugee_total = RefugeeReport.objects.filter(city=city).aggregate(Sum('city_total'))
    city_refugee_total = RefugeeReport.objects.filter(country=country, city=city).aggregate(Sum('city_total'))
    reports = RefugeeReport.objects.filter(country=country, city=city).order_by('year')
    country_totals = Country.objects.filter(refugeereport__city=city).annotate(total=Sum('refugeereport__city_total')).order_by('-total')
    context = {'state': state, 'country': country, 'city': city, 'city_by_year' : city_by_year, 'all_refugee_total': all_refugee_total, 'city_refugee_total': city_refugee_total, 'reports': reports, 'country_totals': country_totals}
    return render(request, 'country_detail.html', context)
