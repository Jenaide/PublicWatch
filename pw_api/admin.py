from django.contrib import admin
from .models import User, MostWanted, MissingPerson

# Register your models here.
admin.site.register(User)
admin.site.register(MissingPerson)
admin.site.register(MostWanted)