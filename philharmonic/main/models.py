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
    pass


class Home(models.Model):
    pass


class Booking(models.Model):
    pass


class Forum(models.Model):
    pass