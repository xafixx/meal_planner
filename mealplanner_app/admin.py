from django.contrib import admin
from .models import Week, Day, Meal

# Register your models here.
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Meal)