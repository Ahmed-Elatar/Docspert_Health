from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import csv
# Create your views here.
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.models import User, Group
from .forms import *
from .models import *
from .serializers import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .task import *






def index(request):
    form=SearchForm()
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            
            return render(request, "search_result.html",{"accounts": search_account(request,form.cleaned_data['account']) })

    
                



    return render( request,"index.html",{"form":form})    

@login_required
def add_csv_file(request):
    form =CsvFileForm()
    if request.method=='POST':
        
        form=CsvFileForm(request.POST,request.FILES)
        file=None

        if form.is_valid():
            
            file = form.save(commit=False)
            file.auth = request.user
            # file.save()
    
            csv_file = form.cleaned_data.get('file')
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            data = list(reader)
            my_task.delay(data)
            
            return redirect('index')




    return render(request , "add_file.html",{"form":form})


@login_required
def make_transfer(request):
    form=TransferForm()
    message=""
    if request.method == 'POST':
        form=TransferForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['accounts_from']," ",form.cleaned_data['accounts_to'] )
            from_ = Account.objects.get(id=form.cleaned_data['accounts_from'].id)
            to_ = Account.objects.get(id=form.cleaned_data['accounts_to'].id)
            print(from_.balance)
            
            if from_.balance >= form.cleaned_data['amount']  and form.cleaned_data['amount'] > 0:
                from_.balance -= form.cleaned_data['amount']
                to_.balance  += form.cleaned_data['amount']
                from_.save()
                to_.save()
                form.save()
                return redirect('index')
            else:
                message ="not-enough"

    return render( request,"make_transfer.html",{"form":form ,"message":message}) 


def list_accounts(request):
    items=Account.objects.all()
    paginator = Paginator(items,25)
    page_number = request.GET.get('page', 1)
    accounts=paginator.page(page_number)





    return render(request,"list_accounts.html",{"accounts":accounts})

def list_transfers(request):
    items=Transfer.objects.all()
    paginator = Paginator(items,25)
    page_number = request.GET.get('page', 1)
    transfers=paginator.page(page_number)

    print(transfers)



    return render(request,"list_transfers.html",{"transfers":transfers,})




def search_account(request, slugg):

    items = Account.objects.filter(name__icontains=slugg) 
    paginator = Paginator(items,3)
    page_number = request.GET.get('page', 1)
    result = paginator.page(page_number)
    
    return result
    













####################################################################################################
##################                  Authentication

#sign-up 
def user_signup(request):
  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
  
        if form.is_valid():
            form.instance.is_staff = True
            user = form.save()
            group = Group.objects.get(name='Normal_Users')
            user.groups.add(group)

            
            return redirect('login')
  
    else:
        form = UserCreationForm()
  
    return render(request, 'signup.html', {'form': form})



# login
def user_login(request):

    if request.user.is_authenticated:
        return redirect ('logout')
  
    if request.method == 'POST':
        

        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
    
            if user:
                login(request, user)    
                return redirect('index')
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    
    logout(request)
    return redirect('login')









