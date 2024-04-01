from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    """
    Includes the list of items for the user.
    """
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/lists/the-only-list-in-the-world/")

    return render(request, "home.html")


def view_list(request):
    """
    View list of items.
    """
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})
