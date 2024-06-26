# Generated by Django 5.0.6 on 2024-06-07 07:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10, unique=True, verbose_name='航班号')),
                ('departure_city', models.CharField(max_length=100, verbose_name='出发城市')),
                ('arrival_city', models.CharField(max_length=100, verbose_name='到达城市')),
                ('departure_time', models.DateTimeField(verbose_name='出发时间')),
                ('arrival_time', models.DateTimeField(verbose_name='到达时间')),
                ('aircraft', models.CharField(max_length=50, verbose_name='机型')),
            ],
            options={
                'verbose_name': '航班信息',
                'verbose_name_plural': '航班信息',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=1, verbose_name='性别')),
                ('id_number', models.CharField(max_length=20, unique=True, verbose_name='证件号')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='电话')),
            ],
            options={
                'verbose_name': '乘客信息',
                'verbose_name_plural': '乘客信息',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_completed', models.BooleanField(default=False)),
                ('seat_preference', models.CharField(choices=[('window', '靠窗'), ('aisle', '靠过道'), ('middle', '中间')], max_length=20, verbose_name='座位位置')),
                ('cabin_class', models.CharField(choices=[('economy', '经济舱'), ('first_class', '头等舱'), ('business', '商务舱')], max_length=20, verbose_name='舱位')),
                ('payment_method', models.CharField(choices=[('wechat', '微信'), ('alipay', '支付宝'), ('bank', '银行卡')], max_length=20, verbose_name='支付方式')),
                ('bank_card_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='银行卡号')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
            ],
            options={
                'verbose_name': '预订信息',
                'verbose_name_plural': '预订信息',
            },
        ),
    ]
