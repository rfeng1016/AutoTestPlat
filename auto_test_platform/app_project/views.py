from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_project.forms import ProjectForm
from app_project.models import Project

# Create your views here.


"""
项目管理
"""
@login_required
def project_manage(request):
    project_all = Project.objects.all()
    return render(request, "project.html", {"projects": project_all,"type": "list"})


"""
添加项目
"""
@login_required
def add_project(request):
    if request.method == "GET":
        return render(request, "project.html", {"type": "add"})
    elif request.method == "POST":
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        if name == "":
            return render(request, "project.html", {"type": "add",
                                                    "name_error": "项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/project/")


"""
删除项目
"""
def delete_project(request, pid):
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)
        except Project.DoesNotExist:
            return HttpResponseRedirect("/project/")
        else:
            project.delete()
        return HttpResponseRedirect("/project/")
    else:
        return HttpResponseRedirect("/project/")


"""
编辑管理
"""
@login_required
def edit_project(request, pid):
    if request.method == "GET":
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectForm(instance=p)
            return render(request, "project.html", {"type": "edit","form": form,"id": pid})

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect("/project/")


"""
项目
"""