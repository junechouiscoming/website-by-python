from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """用户注销"""
    logout(request)
    return HttpResponseRedirect(reverse('my_sites:index'))


def register(request):
    """用户注册"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录后再重定向到主页
            authenticate_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('my_sites:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)