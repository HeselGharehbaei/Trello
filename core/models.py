from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True





