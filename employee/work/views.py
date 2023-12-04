from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Empform,BookForm,PersonForm,StudentForm
from work.models import Emp,Book,Person,Student


# Create your views here.
class Employee(View):
 def get(self,request):
  form=Empform()
  return render(request,"add.html",{"form":form})
 
 def post(self,request):
  print(request.POST)
  form=Empform(request.POST)
  if form.is_valid():
   print(form.cleaned_data)
   Emp.objects.create(**form.cleaned_data)
   #modelname.objects.create(values)
   form=Empform()
   return render(request,"add.html",{"form":form})
  else:
   return render(request,"add.html",{"form":form})
  
class BookView(View):
 def get(self,request):
  form=BookForm()
  return render(request,'book.html',{'form':form})
 def post(self,request):
  form=BookForm(request.POST)
  if form.is_valid():
   form.save()
   form=BookForm()
   """print(form.cleaned_data)
   book=form.cleaned_data.get("title)
   print(book)
   Book.objects.create(**form.cleaned_data)""" #->ORM query

   #form.save() method to add the data into db without using ORM query(only for modelForms)
   # Book.objects.create(**form.cleaned_data)==ORM query

   print("created")
   return render(request,"book.html",{"form":form})
  else:
   return render(request,"book.html",{"form":form})

class Booklist(View):
 def get(self,request):
  qs=Book.objects.all()
  return render(request,"booklist.html",{"qs":qs})
 
class Book_detailedView(View):
 def get(self,request,**kwargs):
# (**kwargs) provides with flexibility to use keyword arguments in our program. Using it as parameter,
# we can eventually pass many arguments(requests)
  id=kwargs.get("pk")
  qs=Book.objects.get(id=id)
  return render(request,"bookd.html",{"data":qs})
 
class Book_delete(View):
 def get(self,request,*args,**kwargs):
  id=kwargs.get("pk")
  Book.objects.get(id=id).delete()
  return redirect('book-al')

class PersonView(View):
 def get(self,request):
  form=PersonForm()
  return render(request,"person.html",{"form":form})
 
 def post(self,request):
  form=PersonForm(request.POST)
  if form.is_valid():
   form.save()
   form=PersonForm()
   print("created")
   return render(request,"person.html",{"form":form})
  else:
   return render(request,"person.html",{"form":form})
  
class Personlist(View):
 def get(self,request):
  ps=Person.objects.all()
  return render(request,"personlist.html",{"ps":ps})
 
class Student(View):
 def get(self,request):
  form=StudentForm()
  return render(request,"student.html",{"form":form})

 def post(self,request):
   form=StudentForm(request.POST)
   if form.is_valid():
    form.save()
    print(form.cleaned_data)
    form=StudentForm()
    return render(request,"student.html",{"form":form})
   else:
    return render(request,"student.html",{"form":form})
  

  