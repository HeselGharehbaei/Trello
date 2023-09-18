from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from core.models import SoftDeleteModel


class User(AbstractUser, BaseModel, SoftDeleteModel):
    email = models.EmailField(
        _("email address"),
        help_text=_("Email address of user"),  
        unique=True,
        blank=True,
    )
    image = models.FileField(
        _("Image"), 
        upload_to="uploads/photos", 
        blank=True, 
        null=True,
    )

    def get_user_owned_workspace(self):
        return self.owned_workspace.all()
    
    def get_user_membered_workspaces(self):
        return self.membered_workspace.all()
    
    def get_completed_task(self):
        return self.tasks.filter(board_list__title="Done", finished_date__isnull=False) 

    def __str__(self):
        return self.username
    