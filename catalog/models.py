import uuid
from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate urls by reversing the URL patterns


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
    address = models.CharField('address',max_length=500, null=True, help_text='address of the temple')
    city = models.CharField(max_length=200, null=True, help_text='city where the temple is located')
    state = models.CharField(max_length=200, null=True, help_text='state where the temple is located')
    country = models.CharField(max_length=200, null=True, help_text='country where the temple is located')
      
    def display_gods(self):
        """
        Creates a string for the god. This is required to display god in Admin.
        """
        return ', '.join([ god.name for god in self.gods.all()[:3] ])
        display_god.short_description = 'god'
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular Temple instance.
        """
        return reverse('Temple-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
        
        
import uuid # Required for unique Temple instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower
