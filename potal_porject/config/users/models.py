from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=150, blank=True)


    
