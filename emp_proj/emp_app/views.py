from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee,Role,Departments

# Create your views here.
def index(request):
    return render(request,"emp_app/index.html")

def all_emp(request):
    employees = Employee.objects.all()
    return render(request, 'emp_app/all_emp.html', {'employees': employees})

from django.contrib import messages
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        location = request.POST.get('location')  # ✅ FIXED
        salary = request.POST.get('salary')
        phone = request.POST.get('phone')

        # Validation for phone number
        if len(phone) != 10 or not phone.isdigit():
            messages.error(request, "❌ Phone number must be exactly 10 digits.")
            return redirect('add_emp')

        # Get related objects
        dept = Departments.objects.get(id=dept_id)
        role = Role.objects.get(id=role_id)

        # Create and save employee
        emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept=dept,
            role=role,
            location=location,
            salary=salary,
            phone=phone
        )
        emp.save()

        messages.success(request, f"✅ {first_name} {last_name} added successfully!")
        return redirect('add_emp')


    departments = Departments.objects.all()
    roles = Role.objects.all()
    return render(request, 'emp_app/add_emp.html', {
        'departments': departments,
        'roles': roles
    })





def delete_emp(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp = get_object_or_404(Employee, id=emp_id)
        emp.delete()
        messages.success(request, f"🗑️ Employee '{emp.first_name} {emp.last_name}' deleted successfully!")
        return redirect('delete_emp')

    employees = Employee.objects.all()
    return render(request, 'emp_app/delete_emp.html', {'employees': employees})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Departments, Role
from django.contrib import messages


def update_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_app/update_list.html', {'employees': employees})

from django.contrib import messages
import re

def update_emp(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    departments = Departments.objects.all()
    roles = Role.objects.all()

    if request.method == 'POST':
        phone = request.POST['phone']

        # Backend validation for phone number
        if not re.fullmatch(r'\d{10}', phone):
            messages.error(request, "❌ Phone number must be exactly 10 digits.")
            return render(request, 'emp_app/update_emp.html', {
                'emp': emp,
                'departments': departments,
                'roles': roles
            })

        # If validation passes, update fields
        emp.first_name = request.POST['first_name']
        emp.last_name = request.POST['last_name']
        emp.dept = Departments.objects.get(id=request.POST['dept'])
        emp.role = Role.objects.get(id=request.POST['role'])
        emp.salary = request.POST['salary']
        emp.phone = phone
        emp.save()

        messages.success(request, f"✅ {emp.first_name} {emp.last_name} updated successfully!")
        return redirect('update_list')

    return render(request, 'emp_app/update_emp.html', {
        'emp': emp,
        'departments': departments,
        'roles': roles
    })
