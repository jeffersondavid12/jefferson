from django.contrib import admin

# Register your models here.
from .models import category, post
class categoryadmin(admin.ModelAdmin):
    readonly_fields = ('createdes', 'updatedes')


class postadmin(admin.ModelAdmin):
    readonly_fields = ('createdes', 'updatedes')
    list_display = ('title', 'author', 'published')



admin.site.register(category,categoryadmin)
admin.site.register(post, postadmin)
