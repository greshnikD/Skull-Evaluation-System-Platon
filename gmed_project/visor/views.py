from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated:
        template = loader.get_template('visor/login.html')
        context = {

        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('visor/visor.html')
        context = {

        }
        return HttpResponse(template.render(context, request))


def visor_page(request):
    if not request.user.is_authenticated:
        template = loader.get_template('visor/login.html')
        context = {

        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')


@csrf_exempt
def login_user(request):
    if request.body:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')
