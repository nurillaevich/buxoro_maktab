from rest_framework import serializers
from .models import Teacher, AboutUs, Category, Course, News, Contact, ContactUs


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'profession', 'fit_back', 'image']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'about']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ['id', 'title', 'category', 'description', 'image']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'image', 'date']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'email', 'phone_number', 'message']