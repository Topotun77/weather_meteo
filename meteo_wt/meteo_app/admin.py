from django.contrib import admin

from .models import UserStat, CityStat, Preferences

# admin.site.register(UserStat)
admin.site.register(CityStat)
admin.site.register(Preferences)


@admin.register(UserStat)
class UserStatAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'period', 'created_at')
    fieldsets = (
        ('Description', {
            'fields': (('user', 'city'), ('period', 'created_at'))
        }),
        # ('Parameters', {
        #     'fields': (('created_at',))
        # })
    )
    search_fields = ('user', 'city')
    list_filter = ('user', 'city', 'period')



# user, city, period, created_at
