# 🔐 Ứng dụng Truyền File Có Ký Số Realtime (Flask + Socket.IO)

Đây là ứng dụng web giúp người dùng **ký số một tệp tin** và **gửi nội dung + chữ ký + public key** đến **người nhận theo thời gian thực** bằng Flask và Socket.IO.

## 🚀 Tính năng
![image](https://github.com/user-attachments/assets/ee206913-cf55-4fa4-82bb-cfcae292f9f9)

- ✅ Người gửi tải file lên → được tạo **chữ ký số** & **public key**
- ✅ Tự động gửi nội dung + chữ ký + public key đến người nhận qua WebSocket
  ![image](https://github.com/user-attachments/assets/b9761c49-8ba5-47a2-9bf0-ade343e0cd9b)

- ✅ Người nhận **nhận realtime** và có thể tải hoặc xác minh file
  ![image](https://github.com/user-attachments/assets/0a362b9c-b9ea-46ad-a03b-3db024634919)

- ✅ Kéo/thả file để kiểm tra xem **có đúng với nội dung đã nhận** không
  ![image](https://github.com/user-attachments/assets/5b1cdb20-7258-4821-93d6-88794892231c)

- ✅ Giao diện hiện đại, trực quan

---

## 🛠 Công nghệ sử dụng

- Python 3.x
- Flask
- Flask-SocketIO
- HTML + CSS + JavaScript
- Crypto (RSA ký số, trong file `utils.py`)

---

## 📂 Cấu trúc thư mục
project/
├── sever.py # Flask app chính
├── utils.py # Xử lý ký số RSA
├── templates/
│ ├── sender.html # Giao diện người gửi
│ └── receiver.html # Giao diện người nhận
├── static/
  └── style.css # Giao diện CSS
