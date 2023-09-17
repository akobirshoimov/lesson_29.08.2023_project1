from django.urls import path
from .views import AllView,DetailUpdateDelView,CreateView

urlpatterns = [
    path('detail/<int:university_id>',DetailUpdateDelView.as_view()),
    # path('all/',all_info)
    path('all/',AllView.as_view()),
    path('create/',CreateView.as_view())
]