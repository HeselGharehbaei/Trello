from django.test import TestCase
from workspaces.models import Workspace
from users.models import User
from models import Board, List, Task, Comment


class TestBoard(TestCase):
    def setup(self):
        self.user1 = User.objects.create(
            username="Ralph",
            password="123456",
        )
        self.user2 = User.objects.create(
            username="Penelope",
            password="111222333",
        )
        self.user3 = User.objects.create(
            username="Felix",
            password="fixitflix",
        )
        self.workspace1 = Workspace.objects.create(
            self.user1,
            "Trello Project",
        )
        self.workspace1.members.add(self.user2)
        self.workspace1.members.add(self.user3)
        self.board1 = Board.objects.create(
            self.workspace1,
            self.user1,
            "Back-end Team",
        )
        self.board2 = Board.objects.create(
            self.workspace1,
            self.user2,
            "Front-end Team",
        )
        self.list1 = List.objects.create(
            self.board1,
            "To Do"
        )
        self.list2 = List.objects.create(
            self.board1,
            "Done",
        )
        self.task1 = Task.objects.create(
            self.list1,
            self.user1,
            "Set SQL Queries",
            "write query set for models",
        )
        self.task1.label.add(self.label1)
        self.task2 = Task.objects.create(
            self.list1,
            self.user2,
            "Write Models",
            "write models for user subsys",
        )
        self.task2.label.add(self.label1)
        self.task2.label.add(self.label2)
        self.comment1 = Comment.objects.create(
            self.task1,
            self.user2,
            "Very well mate",
        )
        self.comment2 = Comment.objects.create(
            self.task1,
            self.user1,
            "Tnx buddy",
        )
        self.label1 = Comment.objects.create(
            self.board1,
            "Office",
            "yellow",
        )
        self.label2 = Comment.objects.create(
            self.board1,
            "Personal",
            "blue",
        )

