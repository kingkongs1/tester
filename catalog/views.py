from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

# Create your views here.

def index(request):  #어떤url요청에대해서 index가 실행되는지 조건을 설정해줘야함
    candidates = Candidate.objects.all()
    context = {'candidates' : candidates}
    return render(request, 'catalog/Test1.html', context)
