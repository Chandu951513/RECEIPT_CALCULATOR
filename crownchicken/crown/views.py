from django.shortcuts import render,redirect
from .models import ammount
from .forms import modelform
from django.db.models import Sum

# Create your views here.


def receipt(request):
    
    basic_amount=(request.POST.get('basic_amount',False))
    if basic_amount == '':
         return render(request,"receipt.html")
    else:
        basic_amount=float(basic_amount)
        saving_amount=float(3.85/100)
        amount_saved=float(int(basic_amount) * saving_amount)
        result_amount=float(basic_amount-amount_saved)
        my=ammount(basic_ammount=basic_amount,saving_amount=saving_amount,ammount_saved=amount_saved,result_amount=result_amount)
        my.save()
        return render(request,"receipt.html",{'result':result_amount,'amount_saved':amount_saved,'basic_ammount':basic_amount})
   
def records(request):
    form=ammount.objects.all()
    total = ammount.objects.all().aggregate(total=Sum('result_amount'))['total']
    return render(request,"data1.html",{'forms':form,'total':total})

def delete(request,pk):
     form=ammount.objects.get(id=pk)
     form.delete()
     return redirect('records')
 
def update(request,pk):
    current=ammount.objects.get(id=pk)
    form=modelform(request.POST or None,instance=current)
    if form.is_valid():
        form.save()
        return redirect('records')
    return render(request,'update.html',{'form':form})
    
     
    

    
        
    
     
