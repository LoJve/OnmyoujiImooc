# _*_coding:utf-8_*_
import unittest

import re

from OnmyoujiImooc import html_downloader, html_parser


class HtmlParserTest(unittest.TestCase):
    root_url = "https://g37simulator.webapp.163.com/get_heroid_list?callback=jQuery1113018601753522716624_1523006109494&rarity=0&page=1&per_page=200&_=1523006109496"
    header_shikigami = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Cookie': '_ntes_nnid=c5b5daeb1272d97430468e1732b568cb,1519825183974; _ntes_nuid=c5b5daeb1272d97430468e1732b568cb; vjuids=62e79541e.16205da9fb2.0.e23af2242a33e8; vjlast=1520516637.1520516637.30; __gads=ID=59c97ce1e0c376c9:T=1520516640:S=ALNI_MY-Ulu5qdgjdVnFyI8fl1cbMrvlgg; __f_=1520606092579; usertrack=ezq0pVqv1lZt26J6F2vwAg==; _ga=GA1.2.882545791.1521473117; __oc_uuid=a45a5000-2d17-11e8-bb06-219006dfa7e9; __utma=187553192.882545791.1521473117.1521644020.1521644020.1; __utmz=187553192.1521644020.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; P_INFO=hjdong8@163.com|1522930382|1|imooc|00&99|jis&1522703808&mail#gud&440300#10#0#0|150232&0|mail&vipmember&mailuni|hjdong8@163.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Host': 'g37simulator.webapp.163.com',
        'Referer': 'https://yys.163.com/shishen/index.html'
    }

    def test_parser_shikigami(self):
        downloader = html_downloader.HtmlDownloader()
        parser = html_parser.HtmlParser()
        response = downloader.download(self.root_url, self.header_shikigami)
        data_dict = parser.parser_shikigami(response.read().decode("utf-8"))
        self.assertIsInstance(data_dict, dict)
        self.assertTrue(len(data_dict) > 0)

    @unittest.skip("don't run")
    def test_re(self):
        text = "妖怪2-天邪鬼绿<天邪鬼绿*1+ 提灯小僧*2>"
        info = re.compile(r'(.*)-(.*)<(.*)>', text)
        self.assertIsNotNone(info.groups())

    def test_re2(self):
        text = "妖怪5(困难)"
        info = re.search(r'\((.*)\)', text)
        self.assertIsNotNone(info.groups())


if __name__ == "__main__":
    unittest.main()
