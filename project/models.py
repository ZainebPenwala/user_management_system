from django.db import models

class Employee(models.Model):
    user_id = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    employee_id = models.CharField(max_length=100, blank=True)
    organisation = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
