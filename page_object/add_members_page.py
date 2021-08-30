# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : add_members_page.py
# @Time       : 2021/8/29 15:38

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.contact_page import ContactPage


class AddMembersPage(BasePage):
    """
    添加成员页面
    """
    _base_url = None

    _menu_contacts = (By.ID, "menu_contacts")

    _username = (By.ID, "username")
    _acctid = (By.ID, "memberAdd_acctid")
    _phone = (By.CSS_SELECTOR, ".ww_telInput_mainNumber")
    _save = (By.CSS_SELECTOR, ".js_btn_save")

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return: 返回通讯录页面实例化对象
        """
        # 点击【通讯录】按钮
        self.find(self._menu_contacts).click()
        return ContactPage(self.browser)

    def add_member(self, name, acctid, phone):
        """
        添加成员操作
        :return: 返回通讯录页面实例化对象
        """
        # 输入姓名
        self.find(self._username).send_keys(name)
        # 输入账号
        self.find(self._acctid).send_keys(acctid)
        # 输入手机号
        self.find(self._phone).send_keys(phone)
        # 点击【保存】按钮
        self.find(self._save).click()
        return ContactPage(self.browser)

    def add_member_fail(self, name, acctid, phone, expect):
        """
        添加成员操作
        :return: 返回通讯录页面实例化对象
        """
        # 输入姓名
        self.find(self._username).send_keys(name)
        # 输入账号
        self.find(self._acctid).send_keys(acctid)
        # 输入手机号
        self.find(self._phone).send_keys(phone)
        # 利用JS将为元素失去焦点
        self.browser.execute_script("arguments[0].blur();", self.find(self._phone))
        # 获取错误提示
        result = self.find(By.XPATH, f"//*[contains(text(),'{expect}')]").text
        return result
