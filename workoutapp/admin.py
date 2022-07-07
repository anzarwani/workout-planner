from django.contrib import admin

from .models import itemTable, workoutTable, planTable

# Register your models here.


admin.site.register(workoutTable)

admin.site.register(itemTable)

admin.site.register(planTable)