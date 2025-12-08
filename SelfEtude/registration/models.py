from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.validators import validate_international_phonenumber 

# Create your models here.
class UserRequirement(AbstractUser):
    Reg_Number = models.CharField(max_length= 9, unique=True, null=False,blank=False)
    phone_number = PhoneNumberField(region='RW', unique=True, null=False, blank=False)
    USERNAME_FIELD = 'Reg_Number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']
    Department ={('Computer Science', 'CS'),
                 ('Information Technology', 'IT'),
                 ('Software Engineering', 'SE'),
                 ('Data Science', 'DS'),
                 ('Information Systems', 'IS')}
    department = models.CharField(max_length=50, choices=Department, null=False, blank=False)
    Level = {('Level 1', 'L1'),
             ('Level 2', 'L2'),
             ('Level 3', 'L3'),
             ('Level 4', 'L4')}
    level = models.CharField(max_length=20, choices=Level, null=False, blank=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userrequirements_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userrequirements_permissions',
        blank=True
    )

    def __str__(self):
        return f"{self.Reg_Number} - {self.first_name} {self.last_name}"

class AttendanceSession(models.Model):
    is_open = models.BooleanField(default=False)
    code = models.CharField(max_length=10, blank=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    closes_at = models.DateTimeField(null=True, blank=True)

    def is_active(self):
        now = timezone.now()
        return self.is_open and self.opened_at <= now <= self.closes_at

    def __str__(self):
        return f"Session {self.id} - Open: {self.is_open}"

class AttendanceRecord(models.Model):
    student = models.ForeignKey(UserRequirement, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Present", "Present"), ("Absent", "Absent")])
    ip = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
    
