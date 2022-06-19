from django.db import models
from django.conf import settings


class Doctor(models.Model):
    fio = models.TextField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    change_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.fio


class Patient(models.Model):
    fio = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    change_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.fio


class ResearchFiles(models.Model):
    real_file_name = models.TextField(blank=True, null=True)
    showed_file_name = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    change_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    versio = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.real_file_name


class Research(models.Model):
    file = models.ForeignKey(ResearchFiles, models.DO_NOTHING)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    version = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    change_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id=}, {self.create_date=}'
