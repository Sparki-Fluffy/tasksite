from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    pub_date = models.DateField()
    event = models.IntegerField()


class Events(models.Model):
    event_title = models.CharField(max_length=40)
    event_date = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=40)


class Actors(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)



class Users(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    # TODO: edit email and password field in table 'Users'
    # email = models.CharField(max_length=120)
    # password = models.CharField(max_length=120)
    rolt = models.CharField(max_length=30)


class Filials(models.Model):
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=256)
    # TODO: add photo


class Home(models.Model):
    # TODO: add poster
    description = models.CharField(max_length=256)
    recommendations = models.CharField(max_length=256)
    # TODO: add photo
    # TODO: add video
    # TODO: add projects


class Booking(models.Model):
    user = models.CharField(max_length=128) # TODO: change after with User table
    event = models.CharField(max_length=128) # TODO: change after with Event table
    count = models.IntegerField()
    status = models.CharField(max_length=64)


class Forum(models.Model):
    pass