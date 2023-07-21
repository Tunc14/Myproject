from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display= ('id','tc','first_name','phone','city','district')
    list_display_links= ('id','tc','first_name')
    search_fields= ('id','tc','first_name','phone','city','district')
    list_per_page= 25