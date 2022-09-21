from django.contrib import admin
from .models import EventCategory, EventTicket

admin.site.register(EventCategory)
admin.site.register(EventTicket)