from django.db import models


class Faculty(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )
    room = models.CharField(max_length=255)
    dept = models.ForeignKey(
        'Department',
        null=True, blank=True,
    )

    def __unicode__(self):
        return 'Faculty: {}'.format(self.name)

    class Meta:
        # instead of calling them "Facultys"
        verbose_name_plural = 'Faculties'


class Department(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        unique=True,
    )
    chair = models.ForeignKey(
        'Faculty',
        null=True, blank=True,
    )

    def __unicode__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text='The first middle and last name of the student'
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
        null=True, blank=True,
    )
    courses = models.ManyToManyField(
        'Course',
        null=True, blank=True,
    )

    def __unicode__(self):
        return 'Student: {}'.format(self.name)



class Course(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )
    students = models.ManyToManyField(
        'Student',
    )
    teacher = models.ForeignKey(
        'Faculty',
        null=False, blank=False,
    )
    department = models.ForeignKey(
        'Department',
        null=True, blank=True,
    )
    number = models.IntegerField(
        default=101,
    )

    def __unicode__(self):
        return '{} {}: {}'.format(
            self.department,
            self.number,
            self.name,
        )