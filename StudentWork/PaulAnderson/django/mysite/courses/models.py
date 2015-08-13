from django.db import models


class Student(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text='The first middle and last name of the student',
    )
    student_id = models.PositiveSmallIntegerField(
        null=False, blank=False,
        unique=True,
    )
    address = models.CharField(
        max_length=255,
    )
    email = models.EmailField(
        max_length=255,
    )
    teaching_assistant = models.BooleanField(
        default=False,
    )
    department = models.ForeignKey(
        'Department',
        null=False, blank=False,
    )
    courses = models.ManyToManyField(
        'Course',
        null=False, blank=False,
    )


class Department(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        unique=True,
    )


class Faculty(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )
    room = models.CharField(max_length=255)
    department = models.ForeignKey('Department')


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        null=True, blank=False,
    )
    students = models.ManyToManyField('Student')
    teacher = models.ForeignKey(
        'Faculty',
        null=True, blank=False,
    )
