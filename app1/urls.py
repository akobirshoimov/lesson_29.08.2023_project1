from django.urls import path
from .views import detail,all_info

urlpatterns = [
    path('detail/<int:school_id>',detail),
    path('all/',all_info)
]