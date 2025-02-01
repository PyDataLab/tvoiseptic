from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', include('main.urls')),
    path('2/', include('city2.urls')),
    path('3/', include('city3.urls')),
    path('4/', include('city4.urls')),
    path('5/', include('city5.urls')),
    path('6/', include('city6.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
