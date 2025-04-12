from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_premium', 'phone', 'address')
    search_fields = ('user__username',)
    list_filter = ('is_premium',)
    readonly_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
