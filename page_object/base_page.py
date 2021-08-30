# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : base_page.py
# @Time       : 2021/8/29 18:11
import os
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

case_yml = "./data/case.yml"


class BasePage:
    """
    基础父类，用于其他类继承公共资源共享
    """
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    _cookies_yml = "./data/cookies.yml"
    _save_filename = f"./data/{time.strftime('%Y-%m-%d %H-%M-%S')}.png"

    def __init__(self, base_browser: WebDriver = None):
        # 判断 driver 对象是否存在
        if base_browser is None:
            # 启动谷歌浏览器
            self.browser = webdriver.Chrome()
            # 设置隐式等待 5 秒
            self.browser.implicitly_wait(5)
            # 最大化浏览器窗口
            self.browser.maximize_window()
            # 打开指定网址
            self.browser.get(self._base_url)
            # 登录企业微信
            self.login()
        else:
            # 存在的话就赋值给当前实例类里
            self.browser = base_browser
            # 如果 _base_url 不为空
            if self._base_url is not None:
                # 如果网页当前的网址和页面类中定义的网址不符，则加载页面类中的网址
                if self.browser.current_url != self._base_url:
                    # 打开指定网址
                    self.browser.get(self._base_url)

    def login(self):
        while True:
            # 判断 cookies.yml 文件是否存在
            if os.path.isfile(self._cookies_yml):
                # 从文件中获取 cookies 信息
                with open(self._cookies_yml) as f:
                    cookies = yaml.safe_load(f)
                # 植入 cookies 到浏览器中，直接免扫码登录
                for cookie in cookies:
                    self.browser.add_cookie(cookie)
            else:
                # 开始人工扫码登录
                print("开始人工扫码登录")

                def wait(x):
                    # 判断是否成功登录
                    return len(x.finds(By.ID, "logout")) > 0

                # 每间隔 1 秒进行一次判断是否已成功登录，超时 60 秒未成功则抛出异常
                WebDriverWait(self, 60, 1).until(wait)
                # 获取浏览器中的 cookies
                cookies = self.browser.get_cookies()
                print(cookies)
                # 将 cookies 写入到一个可持久储存的文件中
                with open(self._cookies_yml, mode="w") as f:
                    yaml.safe_dump(cookies, f)
            # 再次打开后台指定网址
            self.browser.get(self._base_url)
            # noinspection PyBroadException
            try:
                # 使用显式等待查找【退出】按钮，间隔 1 秒查找一次，循环查找 5 秒
                # 如果找到【退出】按钮，则表示为已登录状态
                WebDriverWait(self, 5, 1).until(lambda x: x.find(By.ID, "logout"))
                # 跳出子程序
                return
            except Exception:
                # 登录状态失效过期，删除失效的 cookies.yml 文件
                # 这样进入下一轮循环，就会进入到人工扫码分支了
                os.remove(self._cookies_yml)

    def find(self, by, value=None):
        """
        查找元素
        :param by: 查找方式
        :param value: 元素特征
        :return: 返回元素对象
        """
        if value is None:
            return self.browser.find_element(*by)
        else:
            return self.browser.find_element(by, value)

    def finds(self, by, value=None):
        """
        查找所有符合条件的元素
        :param by: 查找方式
        :param value: 元素特征
        :return: 返回元素对象列表
        """
        if value is None:
            return self.browser.find_elements(*by)
        else:
            return self.browser.find_elements(by, value)

    def SnapShot(self):
        """
        截取浏览器页面快照
        :return: 返回图片文件路径
        """
        self.browser.save_screenshot(self._save_filename)
        return self._save_filename
