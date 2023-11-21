from django.contrib import admin
from grpup.models import Teacher, Student, Group

# Register your models here.

admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Group)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', "contacts", 'groups_list')

    def student_full_name(sels, obj):
        return obj

    def groups_list(self, obj):
        print(obj.id, obj.first_name, obj.last_name, obj.age, obj.contacts)
        print(obj.groups, '!!!')
        # print(Student.objects.all(), '---')
        return [x for  x in obj.groups.all()]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count', 'students_list')

    def students_list(self, obj):
        return [x for x in obj.students.all()]

    def count(self, obj):
        return obj.students.count()

