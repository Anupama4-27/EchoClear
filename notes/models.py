import uuid
from django.db import models
class SecretNote(models.Model):
    id =models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"note{self.id}"
# Create your models here.
