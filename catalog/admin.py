from django.contrib import admin

# Register your models here.
from .models import God, Religion, Temple

admin.site.register(God)
admin.site.register(Religion)

@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    """
    Administration object for BookInstance models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('id', 'name', 'address','summary')
    list_filter = ('gods', 'city')
