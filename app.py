from surch_address import search_address

def main():
    postal_code = input('郵便番号は？(ハイフン無し7桁) ＞')

    address = search_address(postal_code)

    print(address)


if __name__ == '__main__':
    main()
