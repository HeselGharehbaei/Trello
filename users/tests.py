from django.test import TestCase
from .models import User
from boards.models import Board, Task, List
from workspaces.models import Workspace
from datetime import datetime
from django.utils import timezone


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.hesel = User.objects.create(
            username='hesel',
            password='testpass',
            email='hesel@example.com',
        )
        self.pouriya = User.objects.create(
            username='pouriya', 
            password='testpass_2',
            email='pouriya@example.com',
        )
        self.hesel_workspace_1= Workspace.objects.create(owner= self.hesel, title="workspace_1")
        self.hesel_workspace_2= Workspace.objects.create(owner= self.hesel, title="workspace_2")
        self.board_1= Board.objects.create(workspace= self.hesel_workspace_1, owner= self.hesel, title="Board_1" )
        self.list_1= List.objects.create(title= "Done", board= self.board_1)

    def test_get_user_owned_workspace(self):
        owned_workspaces= self.hesel.get_user_owned_workspace()
        list_of_owned_workspaces_title= [workspace.title for workspace in owned_workspaces]
        self.assertEqual(list_of_owned_workspaces_title, ["workspace_1", "workspace_2"])
