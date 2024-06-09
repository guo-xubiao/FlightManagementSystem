# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 获取当前用户的用户名
            current_username = request.user.username
            return redirect('/user_panel/')
            # 可以将当前用户名传递给模板渲染
            # return render(request, 'user_panel/dashboard.html', {'current_username': current_username})
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '注册成功，你现在可以进行登陆啦！')
            return redirect('login')  # 根据你的项目中首页的 URL 名称修改
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
