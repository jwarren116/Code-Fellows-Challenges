from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
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
            return HttpResponseRedirect('index')
    else:
        userinfo = UserForm()
    
    return render(request, 'base.html', {
        'userinfo': userinfo,
        })
