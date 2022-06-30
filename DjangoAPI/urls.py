from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('MyAPI/', include('MyAPI.site.urls')), # for other API names

    path('admin/', admin.site.urls),
    path('', include('MyAPI.urls')), # for our current API
    # path('MyAPI/', include('MyAPI.urls')), # for other API names
    # path('apiname/', MyAPI.site.urls), # for other API names
]
urlpatterns += staticfiles_urlpatterns()

