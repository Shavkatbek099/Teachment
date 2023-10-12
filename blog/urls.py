from django.urls import path
from .views import PostAPIView, TeacherDetailAPIView, StudentListCreateAPIView, StudentRetrieveAPIView

urlpatterns = [
    path("teachers", PostAPIView.as_view(), name="teachers_page"),
    path("teachers/<int:pk>", TeacherDetailAPIView.as_view(), name="teachers_details"),
    path("students/", StudentListCreateAPIView.as_view(), name="Student_list_create_API_View"),
    path("students/<int:pk>", StudentRetrieveAPIView.as_view(), name="Student_retrieve_API_View")
]