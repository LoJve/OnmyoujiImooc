# _*_coding:utf-8_*_
import unittest

from OnmyoujiImooc import data_dealer


class DataDealerTest(unittest.TestCase):
    new_data = {"index": "1", "ratity": "0", "interactive": "0", "name": "test", "icon": "pic_test"}

    def test_collect_data(self):
        dealer = data_dealer.DataDealer()
        self.assertTrue(len(dealer.new_datas)== 0)
        dealer.collect_data(self.new_data)
        self.assertTrue(len(dealer.new_datas) > 0)
        self.assertDictEqual(dealer.new_datas.pop(), self.new_data)



if __name__ == "__main__":
    unittest.main()

