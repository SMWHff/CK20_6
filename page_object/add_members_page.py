# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : add_members_page.py
# @Time       : 2021/8/29 15:38
from dev20_6.page_object.contact_page import ContactPage


class AddMembersPage:
    def goto_contact(self):
        """
        跳转到通讯录页面
        :return: 返回通讯录页面实例化对象
        """
        return ContactPage()

    def add_member(self):
        """
        添加成员操作
        :return: 返回通讯录页面实例化对象
        """
        return ContactPage()