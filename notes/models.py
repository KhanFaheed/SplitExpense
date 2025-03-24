from django.db import models
import uuid

# Create your models here.

class Item(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=100,null=True,blank=True)
    cost=models.FloatField()
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
  

    def __str__(self):
        return self.description

