from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext_lazy as _


class Task(BaseModel, TimeStampMixin):
    list_ = models.ForeignKey(
        "List",
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name=_("List")
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name=_("User")
    )
    title = models.CharField(
        _("Title"),
        help_text=_(" title of task"),
        max_length=50,
    )
    description = models.TextField(
        _("Description"),
        help_text=_("describe your task (optional)"),
        null=True,
        blank=True,
    )
    deadline = models.DateTimeField(
        _("Deadline"),
        help_text = _("specify a deadline (optional)"),
        null=True,
        blank=True,
    )
    start_date = models.DateTimeField(
        _("Start Date"),
        help_text=_("date of start doing task (optional)"),
        null=True,
        blank=True,
    )
    finished_date = models.DateTimeField(
        _("Finish Date"),
        help_text=_("date of when the task finished (optional)"),
        null=True,
        blank=True,
    )
    time_spent = models.TimeField(
        _("Time Spent"),
        help_text=_("the time you spent for doing this task (optional)"),
        null=True,
        blank=True,
    )
    order = models.DecimalField(
        max_digits=7,
        decimal_places=6,
        blank=True,
        null=True,
    )
    label = models.ManyToManyField("Label", blank=True, null=True)

