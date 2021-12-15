from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from authentification.models import Agent
from .models import *


class AgentInline(admin.StackedInline):
    model = Agent
    can_delete = False
    verbose_name_plural = 'agent'


class UserAdmin(BaseUserAdmin):
    inlines = (AgentInline,)


admin.site.register(ArtGraphique)
admin.site.register(ConstatArtGraphique)
admin.site.register(ConstatPeintureSurToile)
admin.site.register(ConstatPeintureSurBois)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Agent)