from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Flight, Passenger, Booking


# 显示航班列表
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})


# 显示航班详情
def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flights/flight_detail.html', {'flight': flight})


# 乘客预订航班
def book_flight(request, flight_id):
    if request.method == 'POST':
        passenger_name = request.POST['passenger_name']
        gender = request.POST['gender']
        id_number = request.POST['id_number']
        phone_number = request.POST['phone_number']
        payment_method = request.POST['payment_method']
        bank_card_number = request.POST.get('bank_card_number', '')
        seat_preference = request.POST['seat_preference']
        cabin_class = request.POST['cabin_class']

        passenger, created = Passenger.objects.get_or_create(
            passenger_name=passenger_name,
            gender=gender,
            id_number=id_number,
            phone_number=phone_number
        )

        flight = get_object_or_404(Flight, id=flight_id)

        booking = Booking.objects.create(
            flight=flight,
            user=request.user,
            departure_date=flight.departure_time,
            seat_preference=seat_preference,
            cabin_class=cabin_class,
            payment_method=payment_method,
            bank_card_number=bank_card_number
        )

        # 返回 JSON 响应，表示预订成功
        return JsonResponse({'success': True})

    return render(request, 'flights/book_flight.html', {'flight_id': flight_id})


def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking and booking.status == 'pending':  # 确保订单存在且状态为待出行
        booking.status = 'cancelled'  # 更新订单状态为已取消
        booking.save()
    return redirect('dashboard')  # 重定向回仪表板页面
