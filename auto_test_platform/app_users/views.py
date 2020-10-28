from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

# 登录首页

def index(request):

    if request.method == "GET":
        return render(request,"index.html")
    else:
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "username or password null"})

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "username or password error"})
        else:
            # 记录用户的登录状态
            auth.login(request, user)
            return HttpResponseRedirect("/project/")


# 处理用户的退出

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")