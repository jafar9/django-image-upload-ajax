from django.shortcuts import render
from myapp.forms import ProfileForm
from myapp.models import Profile
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse




def index(request):
    template='index.html'
    return render(request,template)
# Create your views here.
def create_user(request):
    print('entered into create_user')
    import pdb;pdb.set_trace()
    if request.method == 'POST':
        picture=request.FILES['img']
        return JsonResponse({'cats':192, 'dogs': 300})
    else:
        print('not valid form')
    return JsonResponse({'cats':192, 'dogs': 300})
