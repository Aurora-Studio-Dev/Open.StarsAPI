from requests import *
url = "http://127.0.0.1:5000/v1/news"
back = get(url=url)
print(back.text)