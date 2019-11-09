import unittest

from surch_address import search_address


class TestAddressSerch(unittest.TestCase):
    def test_郵便番号から地名をを検索できる(self):
        self.assertEqual('岩手県八幡平市大更', search_address(zipcode='0287111'))


if __name__ == '__main__':
    unittest.main()
