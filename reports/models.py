from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=255, blank=True, null=True)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name

class State(models.Model):
    name=models.CharField(max_length=255, blank=True, null=True)
    name_slug=models.SlugField()
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/reports/%s/" % (self.name_slug)

class City(models.Model):
    state=models.ForeignKey(State, on_delete=models.CASCADE)
    name=models.CharField(max_length=255, blank=True, null=True)
    name_slug=models.SlugField()
    class Meta:
        ordering = ['state__name', 'name']
    def __str__(self):
        return "%s, %s" % (self.name, self.state.name)
    def get_absolute_url(self):
        return "/reports/%s/%s/" % (self.state.name_slug, self.name_slug)

class RefugeeReport(models.Model):
    country=models.ForeignKey(Country)
    state=models.ForeignKey(State, blank=True, null=True)
    city=models.ForeignKey(City, blank=True, null=True)
    year=models.CharField(max_length=255, blank=True, null=True)
    city_total=models.IntegerField(default=0, null=True)
    state_total=models.IntegerField(default=0, null=True)
    country_total=models.IntegerField(default=0, null=True)
    all_countries=models.IntegerField(default=0, null=True)
    def __str__(self):
        return "%s, %s from %s" % (self.city, self.state, self.year)
    def get_absolute_url(self):
        return "/reports/%s/%s/%s" % (self.city.name_slug, self.state.name_slug, self.year)

class StateCityCountry(models.Model):
    #This exists only to make Bakery happy. Don't use it for anything else.
    state = models.ForeignKey(State)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    def __str__(self):
        return "%s, %s, %s" % (self.state, self.city, self.country)
    def get_absolute_url(self):
        return "/reports/%s/%s/%s/" % (self.state.name_slug, self.city.name_slug, self.country.name_slug)
