from django.shortcuts import render 
from . models import Student
from .forms import StudentForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView 
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class HomePage(TemplateView):
    template_name= "homepage.html"


class AddStudent(SuccessMessageMixin, CreateView):
    model= Student 
    template_name='add_student.html'
    fields= ['name','address','roll','grade', 'email','gender','dob','pic']
    success_message= "1 Student(s) added successfully !!!"
    success_url='/addstudent/'
    
    
class StudentList(ListView):
    model= Student 
    template_name= 'student_list.html'
   
    
class StudentDetail(DetailView):
    model= Student 
    template_name='student_detail.html'        
    
class StudentUpdate(UpdateView):
    model= Student 
    #form_class= StudentForm 
    template_name='update_student.html'
    fields= ['name','address','roll','grade', 'email','gender','dob','pic']
    #success_message= " 1 student(s) record updated successfully !!!"
    success_url='/studentlist/'    
    
    
class StudentDelete(DeleteView):
    model= Student 
    template_name='del_student.html'
    #success_message= " 1 student(s) record deleted successfully !!!"
    success_url= '/studentlist/'    