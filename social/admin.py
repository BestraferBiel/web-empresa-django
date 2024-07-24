from django.contrib import admin
from .models import Link
# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('key', 'name')
    ordering = ('name',)
    search_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)