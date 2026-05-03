from django.contrib import admin
from django.urls import path
from groups.views import group_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', group_list),
]