from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse


# Create your views here.
@login_required
def view_cart(request):
    """View that displays cart contents"""

    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""

    # Get Quantity and Size
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = [int(cart[id][0]) + quantity, size]
    else:
        cart[id] = cart.get(id, [quantity, size])

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified
    amount"""

    # Get Quantity and Size
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    size = cart[id][1]

    if quantity > 0:
        cart[id] = quantity, size
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, id):
    """ Delete a specific product from the cart """

    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
