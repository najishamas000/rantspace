from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Project, Drawing, Essay, Video
from .forms import NewProjForm
from . import genesis
from django.urls import reverse
# Create your views here.
def index(request):
    project_list = Project.objects.all()
    context = { 'project_list': project_list, }
    return render(request, 'rantspace/index.html', context)
def project_detail(request, _prName):
    proj = get_object_or_404(Project, proj_name=_prName)
    return render(request, 'rantspace/details.html', {'proj':proj})
def create_project(request):
    if request.method == 'GET':
        form = NewProjForm()
        context = {'form':form}
        return render(request, 'rantspace/create.html', context)
    elif request.method == 'POST':
        _prName = genesis.generate_id()
        form = NewProjForm(request.POST)
        context = {'form':form, 'proj_name':_prName}
        if form.is_valid():
            hndl = form.cleaned_data['creator_handle']
            _p = Project(proj_name=_prName, gen_date = datetime.now(), creator_handle=hndl)
            _p.save()
            get_proj = get_object_or_404(Project, proj_name=_prName)
            return render(request, 'rantspace/new_project.html', {'proj':get_proj})
    

