from django.conf.urls import url
from django.urls import path
from login_test_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns 

app_name = 'login_test_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('warn/', views.warn, name='warn'),
    path('profile/', views.profile, name='profile'),
  
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)