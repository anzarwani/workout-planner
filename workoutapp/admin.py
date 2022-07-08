from django.contrib import admin

from .models import itemTable, planTable

# Register your models here.


admin.site.register(itemTable)

admin.site.register(planTable)