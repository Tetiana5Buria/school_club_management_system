from django import forms
from .models import Student,Club,Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'class_name']
class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name','description']
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'club']
