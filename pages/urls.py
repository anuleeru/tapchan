
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('', home_page, name='home'),
   path('tapchans/',tapchans,name='tapchans'),
   path('tapchan/<int:id>/',tapchan,name='tapchan'),
   path('order/<int:id>/',order,name='order'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

