from django.db import models


class GenderChoices(models.TextChoices):
    MALE = 'm', 'Male'
    FEMALE = "f", 'Female'


class LevelChoices(models.IntegerChoices):
    FIRST = 1, '1'
    SECOND = 2, '2'
    THIRD = 3, '3'
    FOURTH = 4, '4'


class StatusChoices(models.TextChoices):
    ACTIVE = 'active', 'Active'
    INACTIVE = "inactive", 'inactive'


class DepartmentChoices(models.TextChoices):
    AI = 'AI', 'AI'
    CS = 'CS', 'CS'
    IS = 'IS', 'IS'
    IT = 'IT', 'IT'
    DS = 'DS', 'DS'
