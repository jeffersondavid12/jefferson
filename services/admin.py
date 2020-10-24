from django.contrib import admin

# Register your models here.
from services.models import services
class serviceadmin(admin.ModelAdmin):
    readonly_fields = ('createdes', 'updatedes')
admin.site.register(services,serviceadmin)