from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from userapplication.models import UserDetail


class UserForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['id', 'fname', 'lname', 'email']


def index(request):
    if request.method == 'POST':
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            userinfo.save()
    return render(request, 'base_site.html', {
        'users': UserDetail.objects.order_by('id'),
    })


def detail(request, id):
    try:
        user = UserDetail.objects.get(pk=id)
        form = UserForm(instance=user)
    except UserDetail.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {
        'user': user,
        'form': form,
    })


def update(request, id):
    if request.method == 'POST':
        user = UserDetail.objects.get(pk=id)
        userinfo = UserForm(request.POST)
        if userinfo.is_valid():
            user.fname = request.POST['fname']
            user.lname = request.POST['lname']
            user.email = request.POST['email']
            user.save()
        return HttpResponseRedirect('/userapplication/')


def delete(request, id):
    user = UserDetail.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect('/userapplication/')    
