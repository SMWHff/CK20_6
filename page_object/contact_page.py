# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : contact_page.py
# @Time       : 2021/8/29 15:39



class ContactPage:
    def goto_add_members(self):
        """
        跳转到添加成员页面
        :return: 返回通讯录页面对象实例
        """
        # 防止循环引用对象实例，需要在方法内部进行包导入操作
        from dev20_6.page_object.add_members_page import AddMembersPage
        return AddMembersPage()

    def get_members(self):
        """
        返回成员列表
        :return: 返回用于断言的数据
        """
        return ["SMWHff"]