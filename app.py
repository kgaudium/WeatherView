from flask import Flask, render_template, request, jsonify, url_for
from waitress import serve
import os
from dotenv import load_dotenv
import weather_view
import weather.location

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')


def load_project_dotenv():
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)


@app.route('/get-icon-filename', methods=["POST"])
def get_icon_filename():
    data = request.get_json()

    file_url = url_for('static', filename=f"icons/weather/{data['filename']}.svg")
    return jsonify(file_url)


@app.route('/get-weather-by-ip', methods=["POST"])
def get_weather_by_ip():
    # gets ip address
    data = request.get_json()

    location = weather.location.search_location_by_ip(data["ip"])
    result = weather_view.get_weather_json(location)
    return result


@app.route('/get-weather-by-name', methods=["POST"])
def get_weather_by_name():
    # gets search input
    data = request.get_json()

    location = weather.location.search_location_by_name(data["name"])
    return weather_view.get_weather_json(location)


@app.route('/')
@app.route('/index')
def index():
    # return get_user_ip()
    return render_template('index.html')


if __name__ == '__main__':
    # app.run()
    serve(app, host="127.0.0.1", port=5000)
