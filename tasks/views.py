from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Club,Enrollment
from .forms import StudentForm,ClubForm,EnrollmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def home(request):
 return render(request, 'tasks/home.html')


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'tasks/student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'tasks/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
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
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'tasks/student_confirm_delete.html', {'student': student})
@login_required
def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'tasks/club_list.html', {'clubs': clubs})

@login_required
def club_create(request):
    form = ClubForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('club_list')
    return render(request, 'tasks/club_form.html', {'form': form})

@login_required
def club_update(request, pk):
    club = get_object_or_404(Club, pk=pk)
    form = ClubForm(request.POST or None, instance=club)
    if form.is_valid():
        form.save()
        return redirect('club_list')
    return render(request, 'tasks/club_form.html', {'form': form})

@login_required
def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk)
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
        .order_by('-date_joined')
    )
    return render(request, 'tasks/enrollment_list.html', {'enrollments': enrollments})



# створення
@login_required
def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

    return render(request, 'tasks/enrollment_form.html', {'form': form})


# видалення
@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')

    return render(request, 'tasks/enrollment_confirm_delete.html', {'enrollment': enrollment})
# реєстр

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})
