from django import forms
from work.models import Book,Person,Student

class Empform(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.CharField()

"""class BookForm(forms.Form):
title=forms.CharField()
author=forms.CharField()
publication_year=forms.CharField()
genre=forms.CharField()"""

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

#OR
#fields=['title','author','publication_year','genre']

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields='__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
