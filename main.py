from flask import Flask, render_template
from weather import weather_bp
from dailysentence import daily_sentence_bp
from news import news_bp
from flask_cors import CORS
from flask_sslify import SSLify

app = Flask(__name__)
CORS(app)
sslify = SSLify(app)

app.register_blueprint(weather_bp, url_prefix='/')
app.register_blueprint(daily_sentence_bp, url_prefix='/')
app.register_blueprint(news_bp, url_prefix='/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)