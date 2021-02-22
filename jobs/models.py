from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Pozitie(models.Model):
    companie = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='images/', blank=True, null=True)
    denumirea_pozitiei = models.CharField(max_length=50, blank=True, null=True)
    locatie = models.CharField(max_length=50, blank=True, null=True)
    descrierea_jobului = RichTextUploadingField(max_length=5000, blank=True, null=True)
    promovat = models.BooleanField(default=False)

    def __str__(self):
        return self.companie + " " + self.pozitie + " " + self.locatie

    class Meta:
        verbose_name = 'Pozitie'
        verbose_name_plural = 'Pozitii'

class JobUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    linkedin_profile = models.CharField(max_length=200, null=True, blank=True)

    # class Meta:
    #     fields = ('username', 'linkedin_profile', 'password1', 'password2', 'cv')
