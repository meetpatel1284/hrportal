from django.contrib import admin
from django.urls import path,include
from .views import UserDetailCreationView,UserDetailListView,UserRelativeCreateView,CelebrationCreationView,CelebrationListView,CelebrationParticipantsCreateView
from .views import LeaveCreateView,LeaveListView,RelationTypeCreateView,AttendanceCreateView,AttendanceListView,UpdateStatusView
from . import views


urlpatterns = [
    path("create/",UserDetailCreationView.as_view(),name="userdetail_create"),
    path("list/",UserDetailListView.as_view(),name="userdetail_list"),
    path("create_relative/",UserRelativeCreateView.as_view(),name="employee_relative_create"),
    path("create_relationtype/",RelationTypeCreateView.as_view(),name="employee_relationtype_create"),
    path("delete/<int:pk>/",views.UserDetailDeleteView.as_view(),name="delete_userdetail"),
    path("update/<int:pk>/",views.UserDetailUpdateView.as_view(),name="update_userdetail"),
    path("detail/<int:pk>/",views.UserDetailDetailView.as_view(),name="detail_userdetail"),
    path("celebration_create/",CelebrationCreationView.as_view(),name="celebration_create"),
    path("celebration_list/",CelebrationListView.as_view(),name="celebration_list"),
    path("celebration_delete/<int:pk>/",views.CelebrationDeleteView.as_view(),name="delete_celebration"),
    path("celebration_detail/<int:pk>/",views.CelebrationDetailView.as_view(),name="detail_celebration"),
    path("celebration_update/<int:pk>/",views.CelebrationUpdateView.as_view(),name="update_celebration"),
    path("create_participants/",CelebrationParticipantsCreateView.as_view(),name="celebration_participants_create"),
    path("leave_create/",LeaveCreateView.as_view(),name="leave_create"),
    path("leave_list/",LeaveListView.as_view(),name="leave_list"),
    path("leave_delete/<int:pk>/",views.LeaveDeleteView.as_view(),name="delete_leave"),
    path("leave_detail/<int:pk>/",views.LeaveDetailView.as_view(),name="detail_leave"),
    path("leave_update/<int:pk>/",views.LeaveUpdateView.as_view(),name="update_leave"),
    path("attendance_create/",AttendanceCreateView.as_view(),name="attendance_create"),
    path("attendance_list/",AttendanceListView.as_view(),name="attendance_list"),
    path("leave_status_update/<int:pk>/",UpdateStatusView.as_view(),name="update_status"),
    
    
   
   
    
] 