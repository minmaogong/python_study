"""
    发送http请求
"""
import requests

# 请求的接口地址
url = "https://v1.hitokoto.cn"
# 请求的参数
params = {"c": "d","encode": "json"}
# 发送请求
# requests.get(url, params=params)
response = requests.request(method="GET", url=url, params=params)
json = response.json()
hitokoto = json["hitokoto"]
from_who = json["from_who"] if json["from_who"] else "未知"
print(f"扎心名言:{hitokoto} 出自:{from_who}")
