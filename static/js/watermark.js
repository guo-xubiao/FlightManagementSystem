document.addEventListener("DOMContentLoaded", function() {
        const watermarkText = "212650190郭旭标"; // 替换为您的名字
        const watermark = document.createElement('div');
        watermark.setAttribute('class', 'watermark');
        watermark.textContent = watermarkText;
        document.body.appendChild(watermark);

        document.addEventListener('mousemove', function(event) {
            watermark.style.top = (event.clientY + 10) + 'px';
            watermark.style.left = (event.clientX + 10) + 'px';
        });
    });