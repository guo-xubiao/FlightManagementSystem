// static/js/delete_booking.js
function confirmBookingDeletion(bookingId) {
    var password = prompt('请输入您的登录密码以确认删除订单', '');
    if (!password) {
        // 如果用户取消了输入密码，则不执行任何操作
        return;
    }
    var encodedPassword = encodeURIComponent(password);
    var form = document.createElement('form');
    form.setAttribute('method', 'POST');
    form.setAttribute('action', '/flights/bookings_delete/');

    var csrfInput = document.createElement('input');
    csrfInput.setAttribute('type', 'hidden');
    csrfInput.setAttribute('name', 'csrfmiddlewaretoken');
    csrfInput.setAttribute('value', document.querySelector('input[name="csrfmiddlewaretoken"]').value);

    form.appendChild(csrfInput);

    var bookingIdInput = document.createElement('input');
    bookingIdInput.setAttribute('type', 'hidden');
    bookingIdInput.setAttribute('name', 'booking_id');
    bookingIdInput.setAttribute('value', bookingId);

    form.appendChild(bookingIdInput);

    var passwordInput = document.createElement('input');
    passwordInput.setAttribute('type', 'hidden');
    passwordInput.setAttribute('name', 'password');
    passwordInput.setAttribute('value', encodedPassword);

    form.appendChild(passwordInput);

    document.body.appendChild(form);
    form.submit();

    setTimeout(function() {
        document.body.removeChild(form);
    }, 1000);
}
