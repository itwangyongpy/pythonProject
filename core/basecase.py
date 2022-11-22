import unittest
import requests
from config import configdata
from common import logger

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        r = cls.requests(method='get',url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={configdata["weixin"]["corpid"]}&corpsecret={configdata["weixin"]["corpsecret"]["meetingroom"]}')
        # r = requests.get(
        #     f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={configdata["weixin"]["corpid"]}&corpsecret={configdata["weixin"]["corpsecret"]["meetingroom"]}')

        cls.token = r.json()["access_token"]

    @classmethod
    def requests(cls, method, url, params=None, data=None, json=None, **args):
        """
        自定义发送请求
        method：请求方法
        url：url地址
        params：请求参数
        data：请求体数据
        json：json格式数据
        **args：其他字典参数
        return：

        """
        method = method.upper()
        if method == "GET":
            res = requests.get(url, params=params, **args)
            #添加日志
            logger.info(f"请求方式：{method},请求url：{url},请求参数：{res.request.body},服务器返回结果：{res.text}")
            return res
        elif method == "POST":
            res = requests.post(url, params=data, json=json, **args)
            #添加日志
            logger.info(f"请求方式：{method},请求url：{url},请求参数：{res.request.body},服务器返回结果：{res.text}")
            return res
