#from django.urls import path
#from . import views
#urlpatterns = [
    
  #  path('',views.blog, name="Blog"),
   
#]

from django.urls import path, include
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
