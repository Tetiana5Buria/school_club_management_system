from django import forms
from .models import Student,Club,Enrollment
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')

        if student_id:
            student_id=student_id.strip()

        if Student.objects.filter(student_id=student_id).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Учень з таким ІПН вже існує")

        return student_id

    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'age', 'class_name']
        widgets = {
            'student_id': forms.TextInput(attrs={
                'placeholder': '1234567890',
                'inputmode': 'numeric'
            }),
            'first_name': forms.TextInput(attrs={'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Прізвище"}),
            'age': forms.NumberInput(attrs={'placeholder': "Вік"}),
            'class_name': forms.TextInput(attrs={'placeholder': "Напр. 5-А"}),
        }

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'club']

class LoginForm(forms.Form):
    login = forms.CharField(label="Логін або Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'example@email.com'})
    )
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(attrs={'placeholder': 'Ваш логін'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувач з таким email вже існує")

        return email