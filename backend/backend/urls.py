from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

def home(request):
    return HttpResponse("Taski is running")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]