from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    # path('MyAPI/', include('MyAPI.site.urls')), # for other API names

    re_path('admin/', admin.site.urls),
    re_path('', include('MyAPI.urls')), # for our current API
    # path('MyAPI/', include('MyAPI.urls')), # for other API names
    # path('apiname/', MyAPI.site.urls), # for other API names
]
