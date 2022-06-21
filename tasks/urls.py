from django.urls import path

from tasks.views import (
    TaskViewCreate,
    TaskViewList,
    TaskUpdate,
)

urlpatterns = [
    path("create/", TaskViewCreate.as_view(), name="create_task"),
    path("mine/", TaskViewList.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdate, name="complete_task"),
]
