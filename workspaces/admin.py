from django.contrib import admin
from .models import Workspace, WorkspacesMembership

admin.site.register(Workspace)
admin.site.register(WorkspacesMembership)