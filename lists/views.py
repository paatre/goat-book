from django.shortcuts import redirect, render

from lists.models import Item, List


def home_page(request):
    """
    Home page view. Renders a form for a new to-do item.
    """
    return render(request, "home.html")


def view_list(request):
    """
    View list of items.
    """
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})


def new_list(request):
    """
    Create a new list.
    """
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect("/lists/the-only-list-in-the-world/")
