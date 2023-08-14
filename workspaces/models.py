from django.db import models
from core.models import BaseModel , TimeStampMixin


class Workspace(BaseModel,TimeStampMixin):
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='owned_workspace')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    members = models.ManyToManyField(
        "users.User", through='WorkspacesMembership', through_fields=('workspace', 'member'),related_name='membered_workspace')


    def get_boards(self):
        return self.boards.all()
    

    def __str__(self):
        return self.title


class WorkspacesMembership(TimeStampMixin, BaseModel):
    class Access(models.IntegerChoices):
        MEMBER = 1           
        ADMIN = 2             


    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE)
    
    member = models.ForeignKey(
        'users.User', related_name='workspace_member',on_delete=models.CASCADE)
    access_level = models.IntegerField(choices=Access.choices, default=1)  
  

    def __str__(self):
        return f'{self.member.username}, {self.Workspace.title}'


    class Meta:
        unique_together = ('workspace', 'member')