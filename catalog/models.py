import uuid
from django.db import models
from django.core.validators import URLValidator, EmailValidator 
from django.urls import reverse #Used to generate urls by reversing the URL patterns
from django.utils.text import slugify

# Create your models here.


class God(models.Model):
    """
    Model representing a Temple god (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter the God or Deity Name (e.g. Shiva, Vishnu, Ganesha,  Fiction)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
        
class Religion(models.Model):
    """
    Model representing a religion (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200, help_text="Enter The temples religion (e.g. Hindu, Jain, Buddhism etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
        
class GeoNames(models.Model):
    """
    Model representing a religion (e.g. English, French, Japanese, etc.)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this address')
    country_code = models.CharField(max_length=2, help_text="Country Code")
    postal_code = models.CharField(max_length=20, help_text="Postal Code")
    place_name = models.CharField(max_length=200, help_text="Place Name")
    state_name = models.CharField(null=True, max_length=100, help_text="State Name")
    state_code = models.CharField(null=True, max_length=20, help_text="State Code")
    county_name = models.CharField(null=True, max_length=100, help_text="County Name")
    county_code = models.CharField(null=True, max_length=20, help_text="County Code")
    community_name = models.CharField(null=True, max_length=100, help_text="Community Name")
    community_code = models.CharField(null=True, max_length=20, help_text="Communityy Code")
    latitude = models.FloatField(null=True, help_text="Latitude")
    longitude = models.FloatField(null=True, help_text="Longitude")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """


class Temple(models.Model):
    """
    Model representing a Temple (but not a specific copy of a Temple).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the Temple")
    gods = models.ManyToManyField(God, help_text="Select a god for this Temple")
    # ManyToManyField used because a god can contain many Temples and a Temple can cover many gods.
    religion = models.ForeignKey('Religion', on_delete=models.SET_NULL, null=True)
    address = models.CharField('address',max_length=500, null=True, help_text='Address of the temple')
    city = models.CharField(max_length=100, null=True, help_text='City where the temple is located')
    state = models.CharField(max_length=100, null=True, help_text='State where the temple is located')
    country = models.CharField(max_length=100, null=True, help_text='Country where the temple is located')
    website = models.CharField(max_length=200, null=True, blank=True, help_text='Website', validators=[URLValidator()])
    email = models.EmailField(max_length=200, null=True, blank=True, help_text='Email', validators=[EmailValidator()])
    contact_numbers= models.CharField(max_length=200, null=True, blank=True, help_text='Profile Picture')
    profile_picture= models.CharField(max_length=200, null=True, blank=True,  help_text='Profile Picture')
    rank= models.IntegerField(default= -1, null=True, help_text='Profile Picture')
    active= models.IntegerField(default=1, null=True, help_text='Active Inactive Flag')
    #slug = models.SlugField(unique=True, help_text='Customer Friendly Link')
      

    def display_gods(self):
        """
        Creates a string for the god. This is required to display god in Admin.
        """
        return ', '.join([ god.name for god in self.gods.all()[:3] ])
        display_god.short_description = 'god'
    

    def get_absolute_url(self):
        return reverse('temple-detail', args=[str(self.id)])
        #return reverse('temple-detail', args=[str(self.id) + '::' + str(self.name)])
    
    def get_short_summary(self):
        """
        return first 100 chars of summary.
        """
        short_summary = self.summary[:200]
        if len(short_summary) < 200:
           short_summary = short_summary + '. ' * ((200 - len(short_summary))// 2) 
        return short_summary

    class Meta:
        ordering = ['-rank']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
        

import uuid # Required for unique Temple instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower
