#!/usr/bin/python3
# -*-coding:utf-8 -*-
import unittest
import  requests
import selenium
import xlrd
import  xlwt
class get_request(unittest.TestCase):
    def setUp(self):
        # self.get_url = 'http://www.baidu.com'
        pass
    def test001(self):
        # url = self.get_url
        # r = requests.get(url)
        # print(1111)

        response = requests.get('http://www.baidu.com')
        print(response.status_code)  # 打印状态码
        print(response.url)  # 打印请求url
        print(response.headers)  # 打印头信息
        print(response.cookies)  # 打印cookie信息
        print(response.text)  # 以文本形式打印网页源码
        print(response.content)  # 以字节流形式打印

        # response = requests.get('http://httpbin.org/get')
        # print(response.text)






if __name__ == "__main__":
    unittest.main()