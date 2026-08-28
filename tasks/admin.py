from django.contrib import admin

from .models import Pilot


class PilotsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(Pilot, PilotsAdmin)
