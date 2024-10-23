from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from root.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('urls')),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL,
                                                                       document_root=STATIC_ROOT)
