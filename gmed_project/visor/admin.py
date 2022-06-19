from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User

from .models import ResearchFiles, Research
from django.contrib.sessions.models import Session


class SessionAdmin(ModelAdmin):
    def user(self, obj):
        session_user = obj.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=session_user)
        return user.email

    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['user', 'session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)
admin.site.register(ResearchFiles)
admin.site.register(Research)
