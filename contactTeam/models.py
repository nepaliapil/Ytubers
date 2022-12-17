from django.db import models
from datetime import datetime
# Create your models here.
class ContactTeam(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    detail_message = models.TextField()
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email