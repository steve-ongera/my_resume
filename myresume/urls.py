
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('steve.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



from django.conf.urls import handler404, handler500

handler404 = 'steve.views.custom_page_not_found'
handler500 = 'steve.views.custom_server_error'