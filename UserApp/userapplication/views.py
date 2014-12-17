from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from userapplication.models import UserDetail


class UserForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['fname', 'lname', 'email']


def index(request):
    if request.method == 'POST':
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            userinfo.save()
            return HttpResponseRedirect('')
    
    return render(request, 'base.html', {
        'users': UserDetail.objects.order_by('lname'),
    })

def detail(request, id):
    try:
        user = UserDetail.objects.get(pk=id)
    except UserDetail.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {
        'user': user
    })

def update(request, id):
    # try:
    #     user = UserDetail.objects.get(pk=id)
    # except UserDetail.DoesNotExist:
    #     raise Http404
    if request.method == 'POST':
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            userinfo.save()
            return render(request, 'detail.html', {
                'user': user,
                'userinfo': userinfo,
            })
