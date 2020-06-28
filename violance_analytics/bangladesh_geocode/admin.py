from django.contrib import admin
from .models import Divisions, Districts, Upzilas, Unions

# Register your models here.

admin.site.register(Divisions)
admin.site.register(Districts)
admin.site.register(Upzilas)
admin.site.register(Unions)