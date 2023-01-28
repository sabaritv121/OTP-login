from django.urls import path

from otp_app import views

urlpatterns = [

    path("", views.register,name="log"),
    path("login_view",views.login_view,name="login_view"),
    path("dash",views.dashboard),
    path("otp/<uid>/",views.otp)


]