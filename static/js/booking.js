// static/js/booking.js
document.addEventListener('DOMContentLoaded', function () {
    const paymentMethodSelect = document.getElementById('payment_method');
    const bankCardGroup = document.getElementById('bank-card-group');
    const bookingForm = document.getElementById('booking-form');
    const successModal = document.getElementById('success-modal');
    const closeModalButton = document.getElementById('close-modal-button');

    paymentMethodSelect.addEventListener('change', function () {
        if (this.value === 'bank') {
            bankCardGroup.style.display = 'block';
        } else {
            bankCardGroup.style.display = 'none';
        }
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // 获取表单数据
        const formData = new FormData(bookingForm);

        // 表单验证
        if (!formData.get('passenger_name') || !formData.get('gender') || !formData.get('id_number') || !formData.get('phone_number') || !formData.get('payment_method') || (formData.get('payment_method') === 'bank' && !formData.get('bank_card_number'))) {
            alert('请填写所有必填项');
            return;
        }

        // 提示用户确认信息
        const confirmation = confirm('请确认您的信息是否正确。\n姓名: ' + formData.get('passenger_name') + '\n性别: ' + (formData.get('gender') === 'M' ? '男' : '女') + '\n证件号: ' + formData.get('id_number') + '\n电话: ' + formData.get('phone_number') + '\n支付方式: ' + (formData.get('payment_method') === 'wechat' ? '微信' : formData.get('payment_method') === 'alipay' ? '支付宝' : '银行卡') + '\n座位位置: ' + (formData.get('seat_preference') === 'middle' ? '中间' : formData.get('seat_preference') === 'window' ? '靠窗' : '靠过道') + '\n舱位: ' + (formData.get('cabin_class') === 'economy' ? '经济舱' : formData.get('cabin_class') === 'first_class' ? '头等舱' : '商务舱'));
        if (!confirmation) {
            return;
        }

        // AJAX 请求
        fetch(bookingForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // 显示预订成功模态框
                successModal.style.display = 'block';
            } else {
                alert('预订失败，请重试。');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('预订失败，请重试。');
        });
    });

    // 当用户点击关闭按钮时，隐藏模态框并返回首页
    closeModalButton.addEventListener('click', function () {
        successModal.style.display = 'none';
        window.location.replace('/user_panel/');
    });
});
