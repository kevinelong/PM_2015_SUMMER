from django.db import models

class Student(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )
    student_id = models.PositiveIntegerField(
        null=False, blank=False,
        unique=True,
    )
    address = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    teaching_assistant = models.BooleanField(
        default=False,
    )
    department = models.ForeignKey(
        'Department',
        null='True', blank='True',
    )
    courses = models.ManyToManyField(
        'Course',
        null='True', blank='True',
    )

    def __unicode__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(
        max_length=50,
        null=True, blank=True,
        unique=True,
    )
    chair = models.ForeignKey(
        'Faculty',
        null='True', blank='True',
    )

    def __unicode__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(
        max_length=255,
        null=True, blank=True,
    )
    room = models.CharField(max_length=255)
    dpt = models.ForeignKey(
        'Department',
        null='True', blank='True',
    )

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(
        max_length=255,
        null=True, blank=True,
    )
    students = models.ManyToManyField(
        'Student',
        null='True', blank='True',
    )
    teacher = models.ForeignKey(
        Faculty,
        null=True, blank=True,
    )
    def __unicode__(self):
        return self.name