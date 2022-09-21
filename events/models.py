import uuid
from django.db import models

class EventCategory(models.Model):

    class Meta:
        verbose_name_plural = "Event categories"
        
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EventTicket(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(EventCategory, on_delete=models.PROTECT, null=False)
    artist = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    reference_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.name
