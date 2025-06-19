from flask import Flask, render_template, request
from flask_socketio import SocketIO
import base64
from utils import generate_keys, sign_data, export_key

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def sender():
    return render_template('sender.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = file.read()

    # Tạo khóa và ký số
    private_key, public_key = generate_keys()
    signature = sign_data(data, private_key)
    pub_key = export_key(public_key)

    # Xác định kiểu dữ liệu (text hoặc base64)
    try:
        file_data = data.decode()
        data_type = 'text'
    except:
        file_data = base64.b64encode(data).decode()
        data_type = 'base64'

    # Gửi dữ liệu qua WebSocket
    socketio.emit('new_signature', {
        'signature': signature.hex() if isinstance(signature, bytes) else signature,
        'pub_key': pub_key.decode() if isinstance(pub_key, bytes) else pub_key,
        'data': file_data,
        'data_type': data_type
    })

    # Trả về trang hiển thị cho người gửi
    return render_template('sender.html',
                           signature=signature.hex() if isinstance(signature, bytes) else signature,
                           pub_key=pub_key.decode() if isinstance(pub_key, bytes) else pub_key,
                           file_data=file_data,
                           data_type=data_type)

@socketio.on('connect')
def on_connect():
    print('🔌 Client connected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
