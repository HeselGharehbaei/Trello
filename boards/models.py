from django.db import models
from core.models import BaseModel, TimeSTampMixin
from django.utils.translation import gettext_lazy as _














































































































class Comment(BaseModel, TimeSTampMixin):
    task = models.ForeignKey(
        "Task",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField(
        verbose_name=_("Comment"),
        help_text=_("enter the comment"),
        max_length=200,
        null=True,
        blank=True,
    )

