from flask import Flask, send_from_directory, jsonify, request
import os

app = Flask(__name__)

# Sayaç değerini Python'da tutuyoruz
counter_value = 0

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

# Sayaç API endpoint'leri
@app.route('/api/counter', methods=['GET'])
def get_counter():
    global counter_value
    return jsonify({'counter': counter_value})

@app.route('/api/counter/increment', methods=['POST'])
def increment_counter():
    global counter_value
    counter_value += 1
    return jsonify({'counter': counter_value, 'message': 'Sayaç artırıldı'})

@app.route('/api/counter/decrement', methods=['POST'])
def decrement_counter():
    global counter_value
    counter_value -= 1
    return jsonify({'counter': counter_value, 'message': 'Sayaç azaltıldı'})

@app.route('/api/counter/reset', methods=['POST'])
def reset_counter():
    global counter_value
    counter_value = 0
    return jsonify({'counter': counter_value, 'message': 'Sayaç sıfırlandı'})

if __name__ == '__main__':
    print("Server başlatılıyor... http://localhost:5000")
    print("Sayaç değeri Python'da tutulacak")
    app.run(debug=True, host='0.0.0.0', port=5000) 