from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import pages.urls


urlpatterns = [
    url(r'^', include(pages.urls, namespace='pages')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
