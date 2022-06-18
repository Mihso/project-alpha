from django.urls import path

from projects.views import(
    ProjectViewList,
    ProjectViewDetail,

)

urlpatterns = [
    path("", ProjectViewList.as_view(), name = "list_projects"),
    path("<int:pk>/", ProjectViewDetail.as_view(), name = "show_project"),
]