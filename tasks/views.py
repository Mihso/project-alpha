from tasks.forms import is_complete_form
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

try:
    from tasks.models import Task
except Exception:
    Task = None

# Create your views here.


class TaskViewCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])


class TaskViewList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


def TaskUpdateView(request, pk):
    if request.method == "POST":
        task = Task.objects.get(pk=pk)
        form = is_complete_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
        else:
            pass
    return redirect("show_my_tasks")
