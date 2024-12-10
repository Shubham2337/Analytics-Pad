
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.base,name="Home"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('aboutus',views.aboutus,name="About Us"),
    path('contactus',views.contactus,name="Contactus"),
    path('login',views.login,name="Login"),
    path('singup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('ipl',views.ipl,name="ipl"),
    path('sales',views.sales,name="sales"),
    path('crypto',views.crypto,name="crypto"),
    path('reset_password',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

   

  
]