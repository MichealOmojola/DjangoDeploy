from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)

urlpatterns = [

    # path('api/', include(router.urls)),
    # path('status/', views.approvereject),
    path('', views.cxcontact, name='form')
    # path('admin/', admin.site.urls)
]
