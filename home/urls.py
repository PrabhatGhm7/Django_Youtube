from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  # new

urlpatterns = [
    
    path('upload/', views.upload, name='upload_video'),
    path('home/',views.home, name= 'home'),
    path('myvideos/', views.userupload),
    path('video/<int:pk>',views.videoview, name= 'video'),
    path('search/',views.search,name= 'search')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

