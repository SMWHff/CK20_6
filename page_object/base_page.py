# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : base_page.py
# @Time       : 2021/8/29 18:11
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """
    基础父类，用于其他类继承公共资源共享
    """

    _base_url = ""

    def __init__(self, base_driver: WebDriver = None):
        # 判断 driver 对象是否存在
        if base_driver is None:
            # 启动谷歌浏览器
            self.driver = webdriver.Chrome()
            # 设置隐式等待 3 秒
            self.driver.implicitly_wait(3)
            # 打开指定网址
            self.driver.get(self._base_url)
            # 通过加载 cookies 跳过扫码页面

        else:
            # 存在的话就赋值给当前实例类里
            self.driver = base_driver
