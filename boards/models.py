














































































































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


class List(BaseModel, TimeSTampMixin):
    board = models.ForeignKey(
        "Board",
        on_delete=models.CASCADE,
        related_name="lists",
    )
    title = models.CharField(
        verbose_name=_("Title"),
        help_text=_("enter the title"),
        max_length=50,
        null=False,
        blank=False,
    ) 
    order = models.DecimalField(
        max_digits=7,
        decimal_places=6,
        blank=True,
        null=True,
    )
