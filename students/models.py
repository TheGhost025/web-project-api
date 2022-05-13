from django.db import models
from .choices import GenderChoices, LevelChoices, StatusChoices, DepartmentChoices


class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    mobile_number = models.CharField(max_length=150)
    birth = models.DateField()
    gpa = models.FhloatField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    level = models.IntegerField(choices=LevelChoices.choices, default=LevelChoices.FIRST)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    department = models.CharField(max_length=2, choices=DepartmentChoices.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

