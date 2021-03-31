from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls', namespace='store')), # EL NAMESPACE ES EL NOMBRE DE APP_NAME EEN STORE.URLS
    path('store/basket/', include('store_basket.urls', namespace='basket')), # EL NAMESPACE ES EL NOMBRE DE APP_NAME EEN STORE_BASKET.URLS
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
