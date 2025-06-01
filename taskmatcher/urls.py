from django.contrib import admin
from django.urls import path
from matcher.views import match_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', match_view, name='match'),
]
