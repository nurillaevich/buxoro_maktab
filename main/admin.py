from django.contrib import admin
from .models import Teacher, AboutUs, Category, Course, News, Contact, ContactUs


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', ]
    list_display_links = ['id', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', ]
    list_display_links = ['id', 'name']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_display_links = ['id', 'email']