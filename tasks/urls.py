from django.urls import path

from tasks.views import(
    TaskViewCreate
)

urlpatterns = [
    path("create/",TaskViewCreate.as_view(), name = "create_task"),
]