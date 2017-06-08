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

class StateCount(models.Model):
    name=models.IntegerField(default=0)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name

class StateCountTotal(models.Model):
    name=models.IntegerField(default=0)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name

class CityCount(models.Model):
    name=models.IntegerField(default=0)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name

class CountryCount(models.Model):
    name=models.IntegerField(default=0)
    name_slug=models.SlugField()
    def __str__(self):
        return self.name

class RefugeeReport(models.Model):
    country=models.ForeignKey(Country)
    state=models.ForeignKey(State)
    city=models.ForeignKey(City)
    year=models.CharField(max_length=255)
    state_count_total=models.IntegerField(default=0)
    state_count=models.IntegerField(default=0)
    city_count=models.IntegerField(default=0)
    country_count=models.IntegerField(default=0)
    def __str__(self):
        return "%s, %s from %s" % (self.city, self.state, self.year)
    def get_absolute_url(self):
        return "/reports/%s/%s/%s" % (self.city, self.state.name_slug, self.year)
