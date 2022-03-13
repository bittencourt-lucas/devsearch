from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def list(request):
    projects  = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def index(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project': project, 'tags': tags}
    return render(request, 'projects/project.html', context)

@login_required(login_url="login")
def create(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects_list')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def update(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_list')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def delete(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('projects_list')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)