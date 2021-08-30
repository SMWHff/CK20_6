# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : index_page.py
# @Time       : 2021/8/29 15:34
from selenium.webdriver.common.by import By

from page_object.add_members_page import AddMembersPage
from page_object.base_page import BasePage
from page_object.contact_page import ContactPage


class IndexPage(BasePage):
    """
    首页
    """
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_members(self):
        """
        跳转到添加成员页面
        :return: 返回添加成员页面实例化对象
        """
        # 点击【添加成员】按钮
        self.find(By.CSS_SELECTOR, "A[node-type='addmember']").click()
        return AddMembersPage(self.browser)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return: 返回通讯录页面实例对象
        """
        return ContactPage(self.browser)
