from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (DetailView,ListView,
UpdateView,DeleteView,CreateView)
from main import models
# Create your views here.
class DeleteCollege(DeleteView):
    model=models.College
    template_name='main/confirm.html'
    success_url='/colleges'
class CollegeUpdate(UpdateView):
    model=models.College
    template_name='main/college_create.html'
    fields='__all__'
    success_url='/colleges'
class StudentUpdate(UpdateView):
    model=models.Student
    template_name='main/student_create.html'
    fields='__all__'
    success_url='/college'   
class CollegeCreate(CreateView):
    model=models.College
    template_name='main/college_create.html'
    fields='__all__'
    success_url='/colleges'
class StudentCreate(CreateView):
    model=models.Student
    template_name='main/student_create.html'
    fields='__all__'
    success_url='/colleges'
class CollegeList(ListView):
    model=models.College
    template_name='main/collge_list.html'
    context_object_name='colleges'
class CollegeDetail(DetailView):
    model=models.College
    template_name='main/college_detail.html'
def index(request):
    return render(request,'main/index.html')