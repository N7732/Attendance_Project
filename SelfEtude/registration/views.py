from django.shortcuts import render,redirect
from .form import FormR
from .form import StudentLoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AttendanceSession, AttendanceRecord
from django.utils import timezone
from datetime import date, timedelta
from django.http import HttpResponse
import random
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = FormR(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            print("User registered successfully.")
        return redirect('login')
    else:
        form = FormR()

    return render(request, 'Registration/registration.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            Regnumber = form.cleaned_data['Reg_Number']
            password = form.cleaned_data['password']
            user = authenticate(request, regnumber=Regnumber, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid registration number or password.")
        else:
            return HttpResponse("Form is not valid.")
        
    else:
        form = StudentLoginForm()
    return render(request, 'Registration/login.html', {'form': form})

@login_required
def home(request):
    student = request.user
    session = AttendanceSession.objects.last()
    records = AttendanceRecord.objects.filter(student=student).order_by('-date')

    context = {
        'session': session,
        'records': records,
    }
    return render(request, 'home.html', context)

@login_required
def do_attendance(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        session = AttendanceSession.objects.last()

        if not session or not session.is_active():
            return HttpResponse("Attendance is closed.")

        if code != session.code:
            return HttpResponse("Invalid attendance code.")

        today = date.today()
        if AttendanceRecord.objects.filter(student=request.user, date=today).exists():
            return HttpResponse("You have already submitted attendance.")

        AttendanceRecord.objects.create(
            student=request.user,
            status="Present",
            ip=request.META.get("REMOTE_ADDR")
        )

        return redirect('home')
    else:
        return HttpResponse("Invalid request method.")

# Admin only: open attendance session
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def open_attendance(request):
    code = str(random.randint(100000, 999999))
    now = timezone.now()
    closes = now + timedelta(minutes=2)  # set time window

    AttendanceSession.objects.create(
        is_open=True,
        code=code,
        opened_at=now,
        closes_at=closes
    )
    return render(request, 'admin_open.html', {'code': code, 'closes': closes})