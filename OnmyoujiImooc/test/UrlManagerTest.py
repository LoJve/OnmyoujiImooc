# _*_coding:utf-8_*_
import unittest

from OnmyoujiImooc import url_manager


class UrlManagerTest(unittest.TestCase):
    root_url = "https://g37simulator.webapp.163.com/get_heroid_list?callback=jQuery1113018601753522716624_1523006109494&rarity=0&page=1&per_page=200&_=1523006109496"

    def test_add_new_url(self):
        urls = url_manager.UrlManager()
        urls.add_new_url(self.root_url)
        self.assertEqual(urls.new_urls.pop(), self.root_url)

    def test_has_new_url(self):
        urls = url_manager.UrlManager()
        self.assertFalse(urls.has_new_url())
        urls.add_new_url(self.root_url)
        self.assertTrue(urls.has_new_url())

    def test_get_new_url(self):
        urls = url_manager.UrlManager()
        self.assertFalse(urls.has_new_url())
        urls.add_new_url(self.root_url)
        self.assertEqual(urls.get_new_url(), self.root_url)


if __name__ == "__main__":
    unittest.main()