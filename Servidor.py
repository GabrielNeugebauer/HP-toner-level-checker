from flask import Flask, jsonify
import subprocess
import json
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def get_json_from_curl(url):
    try:
        result = subprocess.run(
            ['curl', '-k', url],
            capture_output=True,
            text=True,
            check=True
        )
        json_output = result.stdout
        json_output = re.sub(r'([{,]\s*)([a-zA-Z0-9_-]+)\s*:', r'\1"\2":', json_output)
        return json.loads(json_output)
    except Exception:
        return None

def import_status(ip):
    try:
        data = get_json_from_curl(f'https://{ip}/sws/app/information/supplies/supplies.json')
        return {
            "toner": data["toner_black"]["remaining"],
            "drum": data["drum_black"]["remaining"]
        } if data else "Inacessível"
    except Exception:
        return "Inacessível"

@app.route('/status')
def get_status():
    impressoras = {
        'Impressora 1': '10.2.3.1',
        'Impressora 2': '10.2.3.4',
        'Impressora 3': '10.2.3.5'
    }

    status_dict = {nome: import_status(ip) for nome, ip in impressoras.items()}
    return jsonify(status_dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
