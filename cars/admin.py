from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):

	def thumbnail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius: 50px;" >'.format(object.car_photo.url))

	thumbnail.short_description = 'photo'

	list_display = ('id', 'thumbnail' ,'car_title', 'location', 'model', 'year' , 'color', 'price','is_featured', 'created_date')
	list_display_links =('id','thumbnail' ,'car_title')
	search_fields = ('id','car_title', 'location', 'model', 'body_style', 'fuel_type')
	list_filter = ('location', 'model', 'body_style', 'fuel_type')
	list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)
