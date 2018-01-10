from django.conf.urls import url

from drf_sample import views

app_name = 'drf'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login_view'),
    url(r'^detail/$', views.UserDetail.as_view(), name='login_view'),
]