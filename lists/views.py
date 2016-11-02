from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

from lists.forms import ExistingListItemForm, ItemForm, NewListForm
from lists.models import List

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    except ValidationError:
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


