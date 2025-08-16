from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm
from django.views import View
from django.contrib import messages

def hello(request):
    return HttpResponse("hello bhadwe")

class HaloView(View):
    def get(self, request):
        return HttpResponse("Hello Ethiopia")

def home(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation created!")
            return redirect("reservation_home")
    else:
        form = ReservationForm()

    reservations = Reservation.objects.all()  # agar user-specific chahiye to filter karo

    return render(request, "index.html", {
        "form": form,
        "reservations": reservations,
    })

def reservation_cancel(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation permanently deleted.")
        return redirect("reservation_home")
    return render(request, "confirm_delete.html", {"reservation": reservation})
