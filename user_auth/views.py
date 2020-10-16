from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from .forms import EmployeeForm, RegistrationForm, CustomAuthenticationForm
from .models import Employee
from django.contrib import messages
from django.contrib.auth.views import LoginView
import jwt

SECRET_KEY = 'ANTARCTICA123'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


@method_decorator(csrf_exempt, name='dispatch')
class Home(View):
	def get(self, request):
		return render(request, 'home.html')


@method_decorator(csrf_exempt, name='dispatch')
class Signup(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
        else:
            print('registartion form not valid')
        return render(request, 'signup.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class Logout(View):
    def get(self, request):
        print('logging out user with user_id: {}'.format(request.user.id))
        logout(request)
        return render(request, 'logout.html')


@method_decorator(csrf_exempt, name='dispatch')
class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            emp_data = Employee.objects.filter(user_id=user_id).last()  # last updated value
            if emp_data:
                emp_data = emp_data.__dict__
                data = {
                    'first_name': emp_data['first_name'],
                    'last_name': emp_data['last_name'],
                    'email': emp_data['email'],
                    'employee_id': emp_data['employee_id'],
                    'organisation': emp_data['organisation']
                }
                print("data: ", data)
                form = EmployeeForm(initial=data)
            else:
                form = EmployeeForm()
            return render(request, 'dashboard.html', {'form': form})
        else:
            return redirect("/login")

    def post(self, request):
        form = EmployeeForm(request.POST)
        employee_id = request.POST['employee_id']
        # print(employee_id)
        unique_emp_id = Employee.objects.filter(employee_id=employee_id)
        if unique_emp_id:
            color = 'red'
            messages.error(request, "Employee id already exists. Please re-enter a unique employee id")
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                color = 'darkgreen'
                messages.success(request, "Details captured successfully!")
                obj.user_id = request.user.id
                obj.save()
        return render(request, 'dashboard.html', {'form': form}, color)


@method_decorator(csrf_exempt, name='dispatch')
class UserList(View):
    def validate_jwt(self, auth_token):
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            if payload:
                return True
        except jwt.ExpiredSignatureError:
            print('Signature expired. Please log in again.')
            return False
        except jwt.InvalidTokenError:
            print('Invalid token. Please log in again.')
            return False
    
    def get(self, request):
        return render(request, 'authenticate.html')

    def post(self, request):
        if request.method == 'POST':
            print("yes")
            user_token = request.POST['token']
            # print(user_token)
            verify = self.validate_jwt(user_token)
            print(verify)
            if verify == True:
                users = Employee.objects.all()
                user_data = []
                for e in users:
                    user_dict = {}
                    user_dict = {
                        'first_name': e.first_name,
                        'last_name': e.last_name,
                        'email': e.email,
                        'employee_id': e.employee_id,
                        'organisation': e.organisation
                    }
                    user_data.append(user_dict)
                data = {'users': user_data}
                return render(request, 'user_list.html', data)
            else:
                messages.error(request, "Invalid Token. Please log in again.")
                return render(request, 'authenticate.html')
