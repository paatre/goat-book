from django.shortcuts import redirect, render

from lists.models import Item, List


def home_page(request):
    """
    Home page view. Renders a form for a new to-do item.
    """
    return render(request, "home.html")


def view_list(request, list_id):
    """
    View list of items.
    """
    our_list = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": our_list})


def new_list(request):
    """
    Create a new list.
    """
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")


def add_item(request, list_id):
    """
    Add a new item to an existing list.
    """
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=our_list)
    return redirect(f"/lists/{our_list.id}/")
