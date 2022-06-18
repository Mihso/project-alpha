from django.urls import path

from tasks.views import(
    TaskViewCreate,
    TaskViewList,
)

urlpatterns = [
    path("create/",TaskViewCreate.as_view(), name = "create_task"),
    path("mine/",TaskViewList.as_view(), name ="show_my_tasks"),
]