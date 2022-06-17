from django.urls import path

from projects.views import(
    ProjectViewList,

)

urlpatterns = [
    path("", ProjectViewList.as_view(), name = "list_projects"),
]