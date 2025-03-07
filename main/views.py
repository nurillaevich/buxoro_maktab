from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import  Teacher, AboutUs, Category, Course, News, Contact, ContactUs
from .serializers import TeacherSerializer, AboutSerializer, CategorySerializer, CourseSerializer, \
    NewsSerializer, ContactSerializer, ContactUsSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class AboutUsListView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUsListView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer
