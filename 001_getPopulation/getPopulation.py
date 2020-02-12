# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:29:09 2020
"""
import json
import urllib
import urllib.request
import matplotlib.pyplot as plt

# proxies = {
# 'http':'http://<ipaddress>:<proxy port>',
# 'https':'https://<ipaddress>:<proxy port>'
# }

url = "http://api.e-stat.go.jp/rest/2.1/app/json/getStatsData?" # 人口増加割合
appId = "8c70935980fb660421d2b4b732fcff6b40ece009"

# statsDataId = '0003191360' # 犯罪率
statsDataId = '0003312317' # 人口割合

### 設定するキー
keys = {
        "appId"            : appId,
        "lang"             : "J",
        "statsDataId"      : statsDataId,
        "metaGetFlg"       : "Y",
        "cntGetFlg"        : "N",
        "sectionHeaderFlg" : "1"
}


### keys からパラメータ文字列を生成
urlString = urllib.parse.urlencode(keys)
print(urlString)


### 対象URLからページを取得する
# proxy = urllib.request.ProxyHandler(proxies)
# opener = urllib.request.build_opener(proxy)
# urllib.request.install_opener(opener)
resp = urllib.request.urlopen(url + urlString)
respDeco = resp.read().decode('utf8')
respJson = json.loads(respDeco)

### グラフ描画
x_data = []
y_data = []

for value in respJson["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]:
    if value["@area"] == "13000": #(*@area=13000 は東京都
        x_data.append(value["@time"])
        y_data.append(value["$"])
plt.plot(x_data,y_data)