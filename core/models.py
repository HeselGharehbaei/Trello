from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)


    class Meta:
        abstract = True


class TimeStampMixin(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True
                




