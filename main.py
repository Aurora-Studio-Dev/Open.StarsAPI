from flask import Flask
import os

from weather import weather_bp
from dailysentence import daily_sentence_bp

BANNER_FILE = 'banner_printed.txt'

def display_banner():
    if not os.path.exists(BANNER_FILE):
        print("███████╗████████╗ █████╗ ██████╗ ███████╗     █████╗ ██████╗ ██╗")
        print("██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██║")
        print("███████╗   ██║   ███████║██████╔╝███████╗    ███████║██████╔╝██║")
        print("╚════██║   ██║   ██╔══██║██╔══██╗╚════██║    ██╔══██║██╔═══╝ ██║")
        print("███████║   ██║   ██║  ██║██║  ██║███████║    ██║  ██║██║     ██║")
        print("╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝")
        print("                        Aurora Studio")
        print(" GitHub: https://github.com/Aurora-Studio-Dev/Open.StarsAPI")
        print("")
        print("API server is starting...")
        with open(BANNER_FILE, 'w') as f:
            f.write('Banner printed')

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(weather_bp, url_prefix='/')
app.register_blueprint(daily_sentence_bp, url_prefix='/')

if __name__ == '__main__':
    display_banner()
    app.run(host='0.0.0.0', port=5000, debug=True)