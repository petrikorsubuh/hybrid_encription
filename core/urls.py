"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.hybrid_encription import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='home'),
    path('login',views.LoginView.as_view()),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('register',views.RegisterView.as_view(),name='register'),
    path('list_inbox',views.ListInbox.as_view(),name='list_inbox'),
    path('send_message', views.MessageView.as_view(), name='send_message'),
    path('aes_encript', views.AES_View.as_view(), name='aes_encript'),
    path('ntru_encript', views.Ntru_EncriptView.as_view(), name='ntru_encript'),
    path('ntru_decript', views.Decript_NTRU_View.as_view(), name='ntru_decript'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

