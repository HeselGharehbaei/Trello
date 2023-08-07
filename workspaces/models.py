from django.db import models
from core.models import BaseModel , TimeStampMixin


class Workspace(BaseModel,TimeStampMixin):
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='owned_workspace')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    members = models.ManyToManyField(
        "users.User", through='WorkspacesMembership', through_fields=('Workspace', 'member'))



    def __str__(self):
        return self.title


class WorkspacesMembership(TimeStampMixin, BaseModel):
    class Access(models.IntegerChoices):
        MEMBER = 1           
        ADMIN = 2             

    Workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE)
    member = models.ForeignKey(
        'User', on_delete=models.CASCADE)
    access_level = models.IntegerField(choices=Access.choices, default=1)
  

    def __str__(self):
        return f'{self.member.full_name} , {self.project.title}'

    class Meta:
        unique_together = ('project', 'member')