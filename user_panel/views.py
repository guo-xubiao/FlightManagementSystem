# user_panel/views.py
from django.db.models.functions import TruncSecond
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from flights.models import Booking
from user_panel.form import UserProfileForm
from user_panel.models import NewsArticle, UserProfile

from django.shortcuts import render
from django.utils import timezone
from pytz import timezone as pytz_timezone


def dashboard(request):
    # 查询当前用户的待出行订单
    pending_bookings = Booking.objects.filter(user=request.user, status__in=['pending'])

    # 查询当前用户的已完成订单
    completed_bookings = Booking.objects.filter(user=request.user, status='completed')

    # 处理退订逻辑
    if 'cancel_booking_id' in request.POST:
        booking_id = request.POST['cancel_booking_id']
        booking = Booking.objects.get(id=booking_id)
        if booking.status == 'pending':
            booking.status = 'cancelled'
            booking.save()
            # 重定向回仪表板页面
            return redirect('dashboard')

    # 获取当前用户的未完成订单
    upcoming_orders = Booking.objects.filter(user=request.user, status__in=['cancelled'])


    # 渲染模板，并将查询到的订单数据传递给模板
    return render(request, 'user_panel/dashboard.html', {
        'pending_bookings': pending_bookings,
        'completed_bookings': completed_bookings,
        'upcoming_orders': upcoming_orders,
    })


def flight_information(request):
    return render(request, 'flights/flight_list.html')


def aviation_news(request):
    def get_driver():
        options = EdgeOptions()
        options.add_argument("--headless")  # 启用Headless模式
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        return driver

    drive = get_driver()
    drive.get("https://www.carnoc.com/")
    data_list = drive.find_elements(By.CSS_SELECTOR, "#hotnew-ul > li")
    news_articles = []
    for li in data_list:
        link = li.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        text = li.text.strip()
        news_articles.append({'text': text, 'link': link})
    return render(request, 'user_panel/aviation_news.html', {'news_articles': news_articles})


def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # 重定向到用户个人中心页面
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_panel/user_profile.html', {'form': form, 'user_profile': user_profile})
