from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True, verbose_name='航班号')
    departure_city = models.CharField(max_length=100, verbose_name='出发城市')
    arrival_city = models.CharField(max_length=100, verbose_name='到达城市')
    departure_time = models.DateTimeField(verbose_name='出发时间')
    arrival_time = models.DateTimeField(verbose_name='到达时间')
    aircraft = models.CharField(max_length=50, verbose_name='机型')

    class Meta:
        verbose_name = '航班信息'
        verbose_name_plural = '航班信息'

    def __str__(self):
        return f"{self.flight_number} 从 {self.departure_city} 到 {self.arrival_city}"


from django.db import models

class Passenger(models.Model):
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
    ]

    passenger_name = models.CharField(max_length=100, verbose_name='姓名')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别')
    id_number = models.CharField(max_length=20, unique=True, verbose_name='证件号')
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='电话')

    class Meta:
        verbose_name = '乘客信息'
        verbose_name_plural = '乘客信息'

    def __str__(self):
        return self.passenger_name



from django.db import models

class Booking(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('wechat', '微信'),
        ('alipay', '支付宝'),
        ('bank', '银行卡'),
    ]

    SEAT_PREFERENCE_CHOICES = [
        ('window', '靠窗'),
        ('aisle', '靠过道'),
        ('middle', '中间'),
    ]

    CABIN_CLASS_CHOICES = [
        ('economy', '经济舱'),
        ('first_class', '头等舱'),
        ('business', '商务舱'),
    ]

    STATUS_CHOICES = [
        ('pending', '待出行'),
        ('completed', '已完成'),
        ('cancelled', '已取消'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    departure_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    seat_preference = models.CharField(max_length=20, choices=SEAT_PREFERENCE_CHOICES, verbose_name='座位位置')
    cabin_class = models.CharField(max_length=20, choices=CABIN_CLASS_CHOICES, verbose_name='舱位')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='支付方式')
    bank_card_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='银行卡号')

    class Meta:
        verbose_name = '预订信息'
        verbose_name_plural = '预订信息'

    def __str__(self):
        return f"Booking {self.id} - Flight: {self.flight.flight_number}, Departure Date: {self.departure_date}"