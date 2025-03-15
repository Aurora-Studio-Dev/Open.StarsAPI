from flask import Flask
from weather import weather_bp
from dailysentence import daily_sentence_bp
from news import news_bp

def display_banner():
    print("███████╗████████╗ █████╗ ██████╗ ███████╗ █████╗ ██████╗ ██╗")
    print("██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║")
    print("███████╗   ██║   ███████║██████╔╝███████╗███████║██████╔╝██║")
    print("╚════██║   ██║   ██╔══██║██╔══██╗╚════██║██╔══██║██╔═══╝ ██║")
    print("███████║   ██║   ██║  ██║██║  ██║███████║██║  ██║██║     ██║")
    print("╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝")
    print("                                                            ")
    print("GitHub: https://github.com/Aurora-Studio-Dev/Open.StarsAPI")
    print(" ")

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(weather_bp, url_prefix='/')
app.register_blueprint(daily_sentence_bp, url_prefix='/')
app.register_blueprint(news_bp, url_prefix='/')

if __name__ == '__main__':
    display_banner()
    app.run(host='0.0.0.0', port=5000, debug=True)