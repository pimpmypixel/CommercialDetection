from django.conf.urls import url
from django.conf.urls.static import static
from web import settings
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)