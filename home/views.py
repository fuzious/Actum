from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import *
import os

# Create your views here.

def add(request):
    return render(request, "home/guide.html")


def guideA(request):
    module_dir=os.path.dirname(__file__)
    file_path=os.path.join(module_dir,'hack.txt')
    data_file=open(file_path,'r')
    data=data_file.read()
    word=[["0","hello"],["13","yes"],["5","welcome"],["23",'autome'],['7',"run"]]
    print(data)
    ll=[]
    for i in data:
        ll.append(i)
    ll=list(data.split(" "))
    print(ll)

    data_file.close()
    if(request.method == 'POST'):
        form1 = Productform(request.POST)
        if form1.is_valid():
            form1.save()
    else:
        form1 = Productform()
    data = Product2.objects.all()
    # data2 = Product.objects.all()
    m=[]
    m2=[]
    for i in data:
        m.append(i)
    data=[]
    flag=0
    
    for i in ll:
        for j in range(0,5):
            
                if(i==word[j][0]):
                    data.append(word[j][1])
            

        

    # data=Product.objects.all()
    print(data)
    for i in data:
        m2.append(i)
    if(len(m2)>=10):
        m2=m2[-1:-11:-1]
    if(len(m)>=10):
        m=m[-1:-11:-1]
    mylist=[]
    for i in range(min(len(m2),len(m))):
        mylist.append([m[i],m2[i]])
    while(i<len(m)):
        mylist.append([m[i],""])
        i+=1
    while(i<len(m2)):
        mylist.append(["",m2[i]])
        i+=1
    print(mylist)




    return render(request, "home/guideA.html", {'form': form1, 'msg': mylist})


def guideB(request):
    module_dir=os.path.dirname(__file__)
    file_path=os.path.join(module_dir,'hack.txt')
    data_file=open(file_path,'r')
    data=data_file.read()
    word=[["0","hello"],["13","yes"],["5","welcome"],["23",'autome'],['7',"run"]]
    print(data)
    ll=[]
    for i in data:
        ll.append(i)
    ll=list(data.split(" "))
    print(ll)
    data=[]
    for i in ll:
        for j in range(0,5):
            
                if(i==word[j][0]):
                    data.append(word[j][1])
    if(request.method == 'POST'):
        form = Productform2(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Productform2()
    data = Product.objects.all()
    return render(request, "home/guideB.html", {'form': form, 'msg': data,'care':data})
