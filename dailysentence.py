# dailysentence.py
from flask import Blueprint, jsonify, request
import requests

daily_sentence_bp = Blueprint('daily_sentence', __name__)

def fetch_quote_from_quotable():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        return {"quote": data['content'], "author": data['author']}
    except requests.RequestException as e:
        return {"error": f"Error fetching quote from Quotable: {e}"}

def fetch_quote_from_zenquotes():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {"quote": data[0]['q'], "author": data[0]['a']}
    except requests.RequestException as e:
        return {"error": f"Error fetching quote from ZenQuotes: {e}"}

@daily_sentence_bp.route('/v1/daily-sentence', methods=['GET'])
def get_daily_quote():
    quote_type = request.headers.get('type')

    if not quote_type:
        return jsonify({"error": "Missing 'type' query parameter."}), 400

    if quote_type == 'quotable':
        quote = fetch_quote_from_quotable()
    elif quote_type == 'zenquotes':
        quote = fetch_quote_from_zenquotes()
    else:
        return jsonify({"error": "Invalid quote type. Use 'quotable' or 'zenquotes'."}), 400

    return jsonify(quote)