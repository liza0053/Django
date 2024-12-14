from django.contrib import admin
from django.urls import path

from my_project.main.views import index_page, time_page, calc_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('time/', time_page),
    path('calc/', calc_page),
]

