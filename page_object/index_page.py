# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : index_page.py
# @Time       : 2021/8/29 15:34

from dev20_6.page_object.add_members_page import AddMembersPage
from dev20_6.page_object.contact_page import ContactPage


class IndexPage:
    def goto_add_members(self):
        """
        跳转到添加成员页面
        :return: 返回添加成员页面实例化对象
        """
        return AddMembersPage()

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return: 返回通讯录页面实例对象
        """
        return ContactPage()
