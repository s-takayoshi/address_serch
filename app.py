import requests

response = requests.get('http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111')

print(response)
print(response.text)
