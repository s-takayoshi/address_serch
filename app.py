import requests

# postal_code = input('郵便番号を入力してください(ハイフンなし7桁) ＞')
postal_code = '0287302'

response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}')
results = response.json()['results'][0]

都道府県名 = results['address1']
市区町村名 = results['address2']
町域名 = results['address3']

address = f'{都道府県名}{市区町村名}{町域名}'
print(address)

# print(response.json())
