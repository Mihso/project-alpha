from django.urls import path

from projects.views import (
    ProjectViewList,
    ProjectViewDetail,
    ProjectViewCreate,
)

urlpatterns = [
    path("", ProjectViewList.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectViewDetail.as_view(), name="show_project"),
    path("create/", ProjectViewCreate.as_view(), name="create_project"),
]
