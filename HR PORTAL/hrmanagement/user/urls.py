from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView




urlpatterns = [
    path("hr_register/",views.HrRegisterView.as_view(),name="hr_register"),
    path("employee_register/",views.EmployeeRegisterView.as_view(),name="employee_register"),
    
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("hr_dashboard/",views.HrDashboardView.as_view(),name="hr_dashboard"),
    #path("developer-register/",views.DeveloperRegisterView.as_view(),name="developer-register"),
    path("employee_dashboard/",views.EmployeeDashboardView.as_view(),name="employee_dashboard"),
    # path("logout/",LogoutView.as_view(next_page="/user/login"),name="logout"),
    path("employee_dashboard/",views.EmployeeDashboardView.as_view(),name="employee_dashboard"),
    path("logout/",views.logout_view,name="logout"),
    path('status_update/<int:pk>/',views.UpdateTaskStatus.as_view(),name='status_update'),
    path('status_update/<int:pk>/',views.UpdateLeaveStatus.as_view(),name='status_update'),
    path('profile/', views.view_profile, name='profile_view'),

   
    
]