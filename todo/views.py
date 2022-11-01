from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(request):
    items = Item.object.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)
     

def add_item(request):
    if request.method == "POST":
        name = request.POST.get("item_name")
        done = 'done' in request.POST
        item.objects.create(name=name, done=done)
    return render(request, "todo/add_item.html")
