# weather.py
from flask import Blueprint, request, jsonify
from bs4 import BeautifulSoup
from requests import get

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/v1/weather', methods=['GET'])
def get_weather():
    try:
        # 获取请求参数
        sheng = request.args.get('sheng')
        shi = request.args.get('shi')
        
        # 参数校验
        if not all([sheng, shi]):
            return jsonify({
                "error": "Missing parameters",
                "required_params": ["sheng", "shi"]
            }), 400

        # 构造请求URL
        url = f"https://tianqi.moji.com/weather/china/{sheng}/{shi}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
        }

        # 发送网络请求
        response = get(url=url, headers=headers)
        response.raise_for_status()  # 检查HTTP错误

        # 解析页面内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取天气数据
        city_info = soup.select_one('div.search_default em').text.strip()
        city_name = city_info.split('，')[0]
        
        weather_div = soup.find('div', class_='wea_weather')
        temperature = weather_div.find('em').text.strip()
        
        weather_img = weather_div.find('img')
        weather = weather_img['alt'] if weather_img else '未知'

        # 返回标准化响应
        return jsonify({
            "city": city_name,
            "temperature": f"{temperature}℃",
            "weather": weather
        })
        
    except Exception as e:
        # 统一异常处理
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500