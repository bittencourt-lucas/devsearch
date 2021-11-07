from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'E-commerce Website',
        'description': 'Fully functional e-commerce website',
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I build out my portfolio',
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on',
    },
]

def projects(request):
    projects  = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id = pk)
    tags = project.tags.all()
    context = {'project': project, 'tags': tags}
    return render(request, 'projects/project.html', context)
