from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomerForm
from .models import Customer
# Create your views here.
def customer_list(request):
    customers= Customer.objects.all().order_by('id_number')
    return render (request,'customer_list.html',{'customers':customers,})
def search_customer(request):
    if request.method == 'POST':
        search_query=request.POST['search_query']
        customers=Customer.objects.filter(
            Customer.Q(tc_number__icontains=search_query) |
            Customer.Q(first_name__icontains=search_query) | 
            Customer.Q(last_name__icontains=search_query) |
            Customer.Q(phone__icontains=search_query) |
            Customer.Q(city__icontains=search_query) |
            Customer.Q(district__icontains=search_query)
        ).order_by('id_number')
        return render(request, 'customer_list.html', {'customers': customers})
    return redirect('customer_list')
def edit_customer(request, customer_id):
    customer=get_object_or_404(Customer, id_number=customer_id) 
    form = CustomerForm(request.POST or None , instance= customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request,'edit_customer.html',{'form':form,'customer':customer})
def delete_customer(request,customer_id):
    customer= get_object_or_404(Customer,id_number=customer_id)
    customer.delete()
    return redirect('customer_list')
def register_customer(request):
    form= CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request,'register_customer.html',{'form':form})








            