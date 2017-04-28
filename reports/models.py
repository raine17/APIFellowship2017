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
    city=models.ForeignKey(City)
    year=models.IntegerField()
    state_count=models.IntegerField()
    city_count=models.IntegerField()
    def __str__(self):
        return "%s, %s from %s" % (self.city, self.state, self.country)
    def get_absolute_url(self):
        return "/reports/%s/%s/%s" % (self.city.state.name_slug, self.city.name_slug, self.country.name_slug)
