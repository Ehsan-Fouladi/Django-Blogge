from django.contrib import admin
from . import models
# Register your models here.

class TicketComment(admin.SimpleListFilter):
    models = models.Ticket

@admin.register(models.profile)
class profile(admin.ModelAdmin):
    list_display = ("user", "malecode", "image")
    list_filter = ("image", "fider_name",)
    list_editable = ("image",)

admin.site.register(models.Ticket)