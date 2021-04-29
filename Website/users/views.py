from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import random
from django.utils import timezone
from influxdb import InfluxDBClient


db_client = InfluxDBClient(host='127.0.0.1', port="8086")

db_client.switch_database('fence_dekut')
# voltage=7
# db_client.query('SELECT "duration" FROM "fence_dekut"."autogen"."fence_dekut" WHERE time > now() ')
result = db_client.query('select last("voltage") from "fence_dekut"')
voltage = list(result.get_points())[0]['last']

#current=8
#voltage = result.get_points(tags={'user':'arap'})


result = db_client.query('select last("current") from "fence_dekut"')
current = list(result.get_points())[0]['last']

#esult = db_client.query('select last("Current") from "fence_dekut"')
#current=8
#current = result.get_points(tags={'user':'arap'})

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.fence_id = form.cleaned_data.get('fence_id')
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html', {'form':form})
@login_required
def profile(request):
    # combining the edit view with the profile
    return render(request, 'users/profile.html')

@login_required()
def edit(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Update successfull! ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context= {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/edit.html',context)

@login_required()
def dashboard(request):
    context={'voltage': voltage,'current':current}
    return render(request,'users/dashboard.html', context)
