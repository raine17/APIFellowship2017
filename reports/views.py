from django.shortcuts import render, get_object_or_404
from reports.models import Country, State, City, RefugeeReport, StateCityCountry
from django.db.models import Sum
from bakery.views import BuildableListView, BuildableDetailView, BuildableTemplateView

class Index(BuildableListView):
  template_name = "index.html"
  queryset = City.objects.order_by('name')

class ResourcesPage(BuildableTemplateView):
    build_path = 'resources/index.html'
    template_name = 'resources_page.html'

class About(BuildableTemplateView):
    build_path = 'about/index.html'
    template_name = 'about.html'

class Stories(BuildableTemplateView):
    build_path = 'stories/index.html'
    template_name = 'stories.html'

class StateList(BuildableListView):
    build_path = 'reports/index.html'
    template_name = 'state_list.html'
    queryset = State.objects.order_by('name')

class CityList(BuildableDetailView):
    model = State
    template_name = 'city_list.html'
    slug_field = 'name_slug'
    def get_context_data(self, **kwargs):
        context = super(CityList, self).get_context_data(**kwargs)
        context['state_totals'] = RefugeeReport.objects.filter(state__name_slug=self.kwargs.get("state_slug")).values('year').annotate(total=Sum('city_total')).order_by('year')
        context['cities'] = City.objects.filter(state=self.object).order_by('name')
        context['count_cities'] = len(context['cities'])
        context['statewide_sum'] = RefugeeReport.objects.filter(state=self.object).aggregate(total=Sum('city_total'))
        return context

class CountryList(BuildableDetailView):
    model = City
    template_name = 'country_list.html'
    slug_field = 'name_slug'
    def get_object(self):
        return City.objects.all()
    def get_context_data(self, **kwargs):
        context = super(CountryList, self).get_context_data(**kwargs)
        context['countries'] = RefugeeReport.objects.filter(city=self.object)
        context['city_by_year'] = RefugeeReport.objects.filter(city=self.object).values('year').annotate(total=Sum('city_total')).order_by('year')
        context['all_refugee_total'] = RefugeeReport.objects.filter(city=self.object).aggregate(Sum('city_total'))
        context['country_totals'] = Country.objects.filter(refugeereport__city=self.object).annotate(total=Sum('refugeereport__city_total')).order_by('-total')
        return context

class CountryDetail(BuildableDetailView):
    model = StateCityCountry
    template_name = 'country_detail.html'
    def get_context_data(self, **kwargs):
        context = super(CountryDetail, self).get_context_data(**kwargs)
        context['state'] = State.objects.get(name_slug=self.object.state.name_slug)
        context['country'] = Country.objects.get(name_slug=self.object.country.name_slug)
        context['city'] = City.objects.get(id=self.object.city.id)
        context['city_by_year'] = RefugeeReport.objects.filter(city=self.object.city, state=self.object.state).values('year').annotate(total=Sum('city_total')).order_by('year')
        context['all_refugee_total'] = RefugeeReport.objects.filter(city=self.object.city, state=self.object.state).aggregate(Sum('city_total'))
        context['city_refugee_total'] = RefugeeReport.objects.filter(country=self.object.country, city=self.object.city, state=self.object.state).aggregate(Sum('city_total'))
        context['reports'] = RefugeeReport.objects.filter(country=self.object.country, city=self.object.city, state=self.object.state).order_by('year')
        context['country_totals'] = Country.objects.filter(refugeereport__city=self.object.city, refugeereport__city__state=self.object.state).annotate(total=Sum('refugeereport__city_total')).order_by('-total')
        return context

"""
#The isle of abandoned function based views

def index(request):
    cities = City.objects.order_by('name')
    context = {'cities': cities}
    return render(request, 'index.html', context)

def resources_page(request):
    return render(request, 'resources_page.html', {})

def about(request):
    return render(request, 'about.html', {})

def stories(request):
    return render(request, 'stories.html', {})

def state_list(request):
    state = State.objects.order_by('name')
    cities = City.objects.order_by('name')
    context = {'state': state, 'cities': cities}
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
    city_by_year = RefugeeReport.objects.filter(country=country, city=city).values('year').annotate(total=Sum('city_total')).order_by('year')
    all_refugee_total = RefugeeReport.objects.filter(city=city).aggregate(Sum('city_total'))
    city_refugee_total = RefugeeReport.objects.filter(country=country, city=city).aggregate(Sum('city_total'))
    reports = RefugeeReport.objects.filter(country=country, city=city).order_by('year')
    country_totals = Country.objects.filter(refugeereport__city=city).annotate(total=Sum('refugeereport__city_total')).order_by('-total')
    context = {'state': state, 'country': country, 'city': city, 'city_by_year' : city_by_year, 'all_refugee_total': all_refugee_total, 'city_refugee_total': city_refugee_total, 'reports': reports, 'country_totals': country_totals}
    return render(request, 'country_detail.html', context)
"""
