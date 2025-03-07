from django.urls import path
from .views import TeacherListView, AboutUsListView, CategoryListView, CourseListView, NewsListView,\
    ContactCreateView, ContactUsListView

urlpatterns = [
    path('/teacher/', TeacherListView.as_view()),
    path('/about/', AboutUsListView.as_view()),
    path('/category/', CategoryListView.as_view()),
    path('/course/', CourseListView.as_view()),
    path('/news/', NewsListView.as_view()),
    path('/contact/', ContactCreateView.as_view()),
    path('/contactus/', ContactUsListView.as_view())
]