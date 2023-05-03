from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html", "rb") as f:
        return f.read()

@app.route('/api/stop/<int:stop_id>')
def proxy_stop(stop_id):
    res = requests.get(f"https://tfeapp.com/api/website/stop_times.php?stop_id={stop_id}")
    return res.json()

@app.route('/api/colors')
def proxy_colors():
    res = requests.get(f"https://lothianapi.com/routes/all")
    return res.json()

app.run()
