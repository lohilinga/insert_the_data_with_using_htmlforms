from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(topic)

admin.site.register(Website)

admin.site.register(Acces_Records)