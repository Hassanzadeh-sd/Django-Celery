from django.contrib import admin
from django.urls import path
from app.views import celery_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celerytask/', celery_view),
]
