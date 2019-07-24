from django.shortcuts import render,redirect
from .models import Restaurant
from .forms import RestaurantForm

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form=RestaurantForm()#create empy form
    #check if reciving data
    if request.method=="POST":
        form=RestaurantForm(request.POST)#store data in form which I created
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')

    context={
        "create_form":form,
    }
    return render(request, 'create.html', context)
