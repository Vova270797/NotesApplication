from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("main.urls")),

    # admin
    path('_adm1n_/', admin.site.urls),
]
