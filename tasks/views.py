from django.shortcuts import render
from tasks.models import Task
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TaskViewCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "projects/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    def get_success_url(self):
        return reverse_lazy("show_project", args = [self.object.project.id])