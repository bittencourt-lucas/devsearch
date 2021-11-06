from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_information = None
    for project in projectsList:
        if project['id'] == pk:
            project_information = project
    context = {'project': project_information}
    return render(request, 'projects/project.html', context)
