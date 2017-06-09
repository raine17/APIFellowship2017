from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=255)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name

class State(models.Model):
    name=models.CharField(max_length=255)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/reports/%s" % self.name_slug

class City(models.Model):
    state=models.ForeignKey(State)
    name=models.CharField(max_length=255)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/reports/%s/%s" % (self.state.name_slug, self.name_slug)

class RefugeeReport(models.Model):
    country=models.ForeignKey(Country)
    state=models.ForeignKey(State)
    city=models.ForeignKey(City)
    year=models.CharField(max_length=255)
    city_total=models.IntegerField(default=0)
    state_total=models.IntegerField(default=0)
    country_total=models.IntegerField(default=0)
    all_countries=models.IntegerField(default=0)
    def __str__(self):
        return "%s, %s from %s" % (self.city.name_slug, self.state.name_slug, self.year)
    def get_absolute_url(self):
        return "/reports/%s/%s/%s" % (self.city.name_slug, self.state.name_slug, self.year)
