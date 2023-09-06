from django.urls import path
from .views import ListSchoolView,DetailUniversityView

urlpatterns = [
    path('detail/<int:university_id>',DetailUniversityView),
    # path('all/',all_info)
    path('all/',ListSchoolView)

]