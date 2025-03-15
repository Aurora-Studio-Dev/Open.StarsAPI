from flask import Flask, Blueprint, request, jsonify
from bs4 import BeautifulSoup
from requests import get

app = Flask(__name__)
news_bp = Blueprint('news', __name__)

@news_bp.route('/v1/news', methods=['GET'])
def get_news():
    try:
        # 构造请求URL
        url = "https://www.chinanews.com.cn/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
        }

        # 发送网络请求
        response = get(url=url, headers=headers)
        response.raise_for_status()  # 检查HTTP错误
        
        # 显式设置响应的编码为utf-8
        response.encoding = 'utf-8'
        html_content = response.text

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        div_tag = soup.find('div', class_='xwzxdd-dbt one-line-multi-link')
        if div_tag:
            first_a_tag = div_tag.find('a')
            if first_a_tag:
                href = "https:"+first_a_tag.get('href', "No href found")
                content = first_a_tag.get_text(strip=True)
            else:
                href = "No a tags found"
                content = "No a tags found"

        # 返回结果
        return jsonify({
            "title": content,
            "url": href
        }), 200

    except Exception as e:
        # 统一异常处理
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

app.register_blueprint(news_bp)
