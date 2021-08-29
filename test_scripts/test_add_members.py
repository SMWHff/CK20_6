# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : test_add_members.py
# @Time       : 2021/8/29 15:43
from dev20_6.page_object.index_page import IndexPage


class TestAddMembers:
    def test_add_members(self):
        """
        1、在首页点击添加成员按钮
        2、跳转到添加成员页面
        3、填充成员信息（姓名、手机号、账号），并保存
        4、跳转通讯录页面，并返回成员列表
        """
        name_list = IndexPage().goto_add_members().add_member().get_members()
        assert "SMWHff" in name_list