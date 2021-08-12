from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^App1/',include('App1.urls'))
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
