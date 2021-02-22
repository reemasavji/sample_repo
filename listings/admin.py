from django.contrib import admin

# Register your models here.

from listings.models import Listing, Contact

class ListingAdmin(admin.ModelAdmin):
	list_display =('id','title','is_published','price','list_date','realtor','sqft')
	list_display_links = ('id','title')
	list_filter = ('realtor',)
	list_editable = ('is_published','price')
	search_fields = ('title','description','address','state','city','zipcode','price')
	list_per_page = 25

admin.site.register(Listing, ListingAdmin)

admin.site.register(Contact)