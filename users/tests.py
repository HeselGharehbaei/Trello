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

    def test_get_user_membered_workspaces(self):
        self.hesel_workspace_1.members.add(self.pouriya)
        self.hesel_workspace_2.members.add(self.pouriya)
        membered_workspaces= self.pouriya.get_user_membered_workspaces()
        list_of_membered_workspaces_title= [workspace.title for workspace in membered_workspaces]
        self.assertEqual(list_of_membered_workspaces_title, ["workspace_1", "workspace_2"])

    def test_get_completed_task(self):
        Task.objects.create(user= self.hesel, board_list= self.list_1, title= "task_1", finished_date= timezone.make_aware(datetime(2023,10,30, 23, 12, 10)))
        Task.objects.create(user= self.hesel, board_list= self.list_1, title= "task_2", finished_date= timezone.make_aware(datetime(2023,10,30, 23, 40, 10)))
        completed_tasks = self.hesel.get_completed_task()
        completed_tasks_list= [completed_task.title for completed_task in completed_tasks]
        self.assertEqual(completed_tasks_list, ["task_1", "task_2"])   
        