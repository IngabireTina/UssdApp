from django.db import models
from rest_framework import serializers


# Create your models here.
class UssdApplication(models.Model):
    msisdn = models.IntegerField()
    session_id = models.IntegerField()
    code = models.CharField(max_length=40)
    newreq = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.msisdn
    # return str(self.msisdn) + "session:" + str(self.session_id) + "new request: " + str(self.newreq) + "code:" + str(
    #     self.code)


class Task(models.Model):
    msisdn = models.IntegerField()
    session_id = models.IntegerField()
    code = models.CharField(max_length=40)
    newreq = models.CharField(max_length=40)

    def __str__(self):
         return str(self.msisdn) + "session:" + str(self.session_id) + "new request: " + str(self.newreq) + "code:" + str(
         self.code)

