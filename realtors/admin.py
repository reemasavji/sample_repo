from django.contrib import admin

# Register your models here.

from realtors.models import Realtor
class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','email','phone','is_mvp','hire_date')
	list_display_links = ('id', 'name')
	list_filter = ('name',)
	list_editable = ('is_mvp',)
	search_fields = ('name','description','email','phone')
	list_per_page = 25

admin.site.register(Realtor,RealtorAdmin)