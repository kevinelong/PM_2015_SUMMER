from django.contrib import admin

from courses.models import Course, Faculty, Department, Student


class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class FacultyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faculty, FacultyAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)