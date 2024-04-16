from django.db import models


class News(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField()
    pub_date = models.DateField()
    event = models.IntegerField()


class Events(models.Model):
    pass


class Actors(models.Model):
    pass


class Users(models.Model):
    pass


class Filials(models.Model):
    pass


class Home(models.Model):
    pass


class Booking(models.Model):
    pass


class Forum(models.Model):
    pass