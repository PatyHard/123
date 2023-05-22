from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AllWeaponsView, WeaponDetailView

app_name = 'weapons'

urlpatterns = [
    path('', AllWeaponsView.as_view(), name='index'),
    path('weapon/<int:pk>/', WeaponDetailView.as_view(), name='weapon_info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

