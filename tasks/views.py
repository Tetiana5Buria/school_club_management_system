from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Club,Enrollment
from .forms import RegisterForm, StudentForm,ClubForm,EnrollmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm

def landing(request):
    return render(request, 'tasks/landing.html')


def home(request):
 return render(request, 'tasks/home.html')


@login_required
def student_list(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'tasks/student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
           student = form.save(commit=False)
           student.user = request.user
           student.save()
           return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'tasks/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'tasks/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, user=request.user)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'tasks/student_confirm_delete.html', {'student': student})
@login_required
def club_list(request):
    clubs = Club.objects.filter(user=request.user)
    return render(request, 'tasks/club_list.html', {'clubs': clubs})

@login_required
def club_create(request):
    form = ClubForm(request.POST or None)
    if form.is_valid():
        club = form.save(commit=False)
        club.user = request.user
        club.save()
        return redirect('club_list')
    return render(request, 'tasks/club_form.html', {'form': form})

@login_required
def club_update(request, pk):
    club = get_object_or_404(Club, pk=pk, user=request.user)
    form = ClubForm(request.POST or None, instance=club)
    if form.is_valid():
        form.save()
        return redirect('club_list')
    return render(request, 'tasks/club_form.html', {'form': form})

@login_required
def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk, user=request.user)
    if request.method == 'POST':
        club.delete()
        return redirect('club_list')
    return render(request, 'tasks/club_confirm_delete.html', {'club': club})

# список
@login_required
def enrollment_list(request):
    enrollments = (
        Enrollment.objects
        .select_related('student', 'club')
        .filter(student__user=request.user)
        .order_by('-date_joined')
    )
    return render(request, 'tasks/enrollment_list.html', {'enrollments': enrollments})



@login_required
def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)

        form.fields['student'].queryset = Student.objects.filter(user=request.user)
        form.fields['club'].queryset = Club.objects.filter(user=request.user)

        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

        form.fields['student'].queryset = Student.objects.filter(user=request.user)
        form.fields['club'].queryset = Club.objects.filter(user=request.user)

    return render(request, 'tasks/enrollment_form.html', {'form': form})
# видалення
@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')

    return render(request, 'tasks/enrollment_confirm_delete.html', {'enrollment': enrollment})

#іхід



def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login_input = form.cleaned_data['login']
        password = form.cleaned_data['password']

        user = None

        if '@' in login_input:
            try:
                user_obj = User.objects.get(email=login_input)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=login_input, password=password)

        if user:
            login(request, user)
            return redirect('home')

        else:
            form.add_error(None, "Невірний логін або пароль")

    return render(request, 'tasks/login.html', {'form': form})
# реєстр

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if not form.is_valid():
            print(form.errors)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'tasks/register.html', {'form': form})
