from django.contrib import admin

from .models import UserStat, CityStat, Preferences

# admin.site.register(UserStat)
# admin.site.register(CityStat)
admin.site.register(Preferences)


@admin.register(UserStat)
class UserStatAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'period', 'created_at')
    fieldsets = (
        ('Description', {
            'fields': (('user', 'city'), ('period', 'created_at'))
        }),
    )
    search_fields = ('user', 'city')
    list_filter = ('user', 'city', 'period')


@admin.register(CityStat)
class CityStatAdmin(admin.ModelAdmin):
    list_display = ('city', 'query_count', 'latitude', 'longitude')
    fieldsets = (
        ('Description', {
            'fields': ('city', 'query_count')
        }),
        ('Parameters', {
            'fields': ('latitude', 'longitude')
        })
    )
    search_fields = ('city',)
    list_filter = ('city', 'query_count', 'latitude', 'longitude')
