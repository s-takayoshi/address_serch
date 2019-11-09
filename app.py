import requests

postal_code = input('郵便番号を入力してください(ハイフンなし7桁) ＞')

response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}')

print(response)
print(response.text)

