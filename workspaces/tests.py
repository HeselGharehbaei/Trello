from django.test import TestCase
from users.models import User
from .models import Workspace, WorkspacesMembership

class WorkspaceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpass'
        )

        self.workspace = Workspace.objects.create(
            owner=self.user, title='Test Workspace', description='Test Description'
        )

    def test_get_boards(self):
        self.assertEqual(list(self.workspace.get_boards()), [])

    def test_workspaces_membership_creation(self):
        membership = WorkspacesMembership.objects.create(
            Workspace=self.workspace, member=self.user, access_level=WorkspacesMembership.Access.MEMBER
        )

        self.assertEqual(membership.access_level, WorkspacesMembership.Access.MEMBER)
        self.assertEqual(str(membership), f'{self.user.username}, {self.workspace.title}')

    def test_workspaces_membership_unique_together(self):
        membership1 = WorkspacesMembership.objects.create(
            Workspace=self.workspace, member=self.user, access_level=WorkspacesMembership.Access.MEMBER
        )

        with self.assertRaises(Exception):
            membership2 = WorkspacesMembership.objects.create(
                Workspace=self.workspace, member=self.user, access_level=WorkspacesMembership.Access.MEMBER
            )
    
    def test_workspace_str_method(self):
        self.assertEqual(str(self.workspace), 'Test Workspace')

    def test_workspaces_membership_str_method(self):
        membership = WorkspacesMembership.objects.create(
            Workspace=self.workspace, member=self.user, access_level=WorkspacesMembership.Access.MEMBER
        )
        self.assertEqual(str(membership), f'{self.user.username}, {self.workspace.title}')

