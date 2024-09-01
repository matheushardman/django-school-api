from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True, blank = False)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)], blank = False)
    first_grade = models.FloatField(default = 0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True)
    second_grade = models.FloatField(default = 0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True)
    teacher_name = models.CharField(max_length=100, blank = False)
    school_room = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)], blank = False)

    def __str__(self):
        return self.name