from django.contrib import admin
from .models import Listing

# Set admin table what to show
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published', 'price', 'list_date', 'realtor')
    ordering = ('id',)
    search_fields = ('title',)
    list_display_links = ('id', 'title')
    list_editable =('is_published',)
    list_per_page = 25



    # exista sortarea direct in tabel prin click dat pe campul care ne intereseaza
    # Alte optiuni interesante:
    # search_fields = ('title', 'description')
    # list_filter = ('id', 'realtor')

# Register your models here
admin.site.register(Listing, ListingAdmin)
