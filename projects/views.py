from django.shortcuts import render
from projects.models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ProjectViewList(LoginRequiredMixin ,ListView):
    model = Project
    template_name = "projects/list.html"
    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

class ProjectViewDetail(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"