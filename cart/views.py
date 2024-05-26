from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseBadRequest
from booking.models import SpaBookingServices, SpaBooking, SpaService
from decimal import Decimal
from booking.forms import TimeSlotSelectionForm

# Create your views here.

def add_to_cart(request, service_id=None):
    if service_id is None:
        return HttpResponseBadRequest("Service ID is required")

    selected_service = get_object_or_404(SpaService, pk=service_id)

    if request.method == "POST":
        time_slot_form = TimeSlotSelectionForm(request.POST)
        if time_slot_form.is_valid():
            selected_time_slot = time_slot_form.cleaned_data["selected_time_slot"]
            selected_date = request.POST.get("selected_date")
            quantity = request.POST.get("quantity")

            if not selected_date:
                return HttpResponseBadRequest("Date is required")

            if not quantity:
                return HttpResponseBadRequest("Quantity is required")

            spa_service_total = selected_service.price if selected_service.price else 0

            cart = request.session.get("cart", {})
            service_key = f"{selected_service.id}_{selected_date}_{selected_time_slot.time}"

            if service_key in cart:
                cart[service_key]["quantity"] += int(quantity)
            else:
                cart[service_key] = {
                    "spa_service": selected_service.name,
                    "quantity": int(quantity),
                    "spa_service_total": str(spa_service_total),
                    "selected_date": selected_date,
                    "selected_time": selected_time_slot.time,
                }

            request.session["cart"] = cart
            return redirect("view_cart")

    return HttpResponseBadRequest("Invalid request")
    

def update_cart(request, service_id):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        if str(service_id) in cart:
            new_quantity = int(request.POST.get("quantity", 1))
            cart[str(service_id)]["quantity"] = new_quantity
            request.session["cart"] = cart
    return redirect("view_cart")


def view_cart(request):
    cart = request.session.get("cart", {})
    services = []
    total_cost = Decimal("0.00")

    for service_id, details in cart.items():
        try:
            service_total = Decimal(details["spa_service_total"]) * details["quantity"]
            total_cost += service_total
            services.append(
                {
                    "id": service_id,
                    "spa_service": details["spa_service"],
                    "quantity": details["quantity"],
                    "spa_service_total": service_total,
                    "selected_date_and_time": details.get("selected_date_and_time"),
                    "selected_time_slot_id": details.get("selected_time_slot_id"),
                }
            )
        except KeyError as e:
            print(f"Missing key in cart session data: {e}")

    context = {
        "services": services,
        "total_cost": total_cost,
    }
    return render(request, "cart/view_cart.html", context)


def remove_from_cart(request, service_id):
    """
    Remove a specific service from the cart.
    """
    cart = request.session.get("cart", {})
    try:
        if str(service_id) in cart:
            del cart[str(service_id)]
            messages.success(request, "Service removed from cart successfully")
        else:
            messages.error(request, "Service not found in cart")

        request.session["cart"] = cart
        return redirect("view_cart")

    except KeyError:
        messages.error(request, "Service not found in cart")
        return redirect("view_cart")


def clear_cart(request):
    """
    Clears all items from the user's cart stored in the session.

    This view sets the 'cart' key in the session to an empty dictionary,
    effectively removing all services that the user has added to the cart.
    After clearing the cart, the user is redirected to the view_cart page
    to see the updated (empty) cart.

    Used to generate the response.

    Returns:
        HttpResponseRedirect: A redirect response to the 'view_cart' page.
    """

    request.session["cart"] = {}
    return redirect("view_cart")
