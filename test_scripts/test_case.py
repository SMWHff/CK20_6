# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : test_add_members.py
# @Time       : 2021/8/29 15:43

import allure
import pytest
import yaml

from page_object.base_page import case_yml
from page_object.index_page import IndexPage


def get_case_data():
    with open(case_yml, encoding="utf-8") as f:
        case_data = yaml.safe_load(f)
    del_member_data = case_data.get("del_member").get("data")
    del_member_ids = case_data.get("del_member").get("ids")
    add_member_data = case_data.get("add_member").get("data")
    add_member_ids = case_data.get("add_member").get("ids")
    add_member_fail_data = case_data.get("add_member_fail").get("data")
    add_member_fail_ids = case_data.get("add_member_fail").get("ids")
    return \
        del_member_data, del_member_ids, \
        add_member_data, add_member_ids, \
        add_member_fail_data, add_member_fail_ids


class TestCase:
    """
    测试用例
    """

    def setup_class(self):
        # 类创建时调用一次
        # 启动浏览器，并登陆企业微信到首页
        self.index = IndexPage()

    def teardown_class(self):
        # 类销毁时调用一次
        # 关闭浏览器
        self.index.browser.quit()

    # 设置测试用例跳过不执行
    @pytest.mark.skip
    # 设置测试用例功能名
    @allure.feature("被跳过的测试用例")
    def test_demo(self):
        """
        未完工的测试用例
        :return:
        """
        pass

    # 设置测试用例参数化
    @pytest.mark.parametrize("phone", get_case_data()[0], ids=get_case_data()[1])
    # 设置测试用例功能名
    @allure.feature("删除成员成功")
    # 设置测试用例执行顺序
    @pytest.mark.run(order=3)
    def test_del_members(self, phone):
        """
        删除成员测试用例
        1、在首页点击通讯录按钮
        2、跳转到添加通讯录页面
        3、根据手机号勾选成员，点击删除，并操作结果
        """
        with allure.step("进入到首页"):
            index = IndexPage(self.index.browser)
        with allure.step("在首页点击通讯录按钮，跳转到添加通讯录页面"):
            add_members = index.goto_contact()
        with allure.step("根据手机号勾选成员，点击删除，并操作结果"):
            tips = add_members.del_member(phone)
        # 提前预断言判断
        if "删除成功" not in tips:
            # 浏览器截图
            path = self.index.SnapShot()
            # 将截图贴到报告中
            allure.attach.file(path, f"出错：'删除成功' 不符合 '{tips}'", attachment_type=allure.attachment_type.PNG)
        # 进行断言判断
        assert "删除成功" in tips, f"删除成功 in {tips}"

    # 设置测试用例参数化
    @pytest.mark.parametrize("name,acctid,phone", get_case_data()[2], ids=get_case_data()[3])
    # 设置测试用例功能名
    @allure.feature("添加成员成功")
    # 设置测试用例执行顺序
    @pytest.mark.run(order=1)
    def test_add_members(self, name, acctid, phone):
        """
        添加成员测试用例成功
        1、在首页点击添加成员按钮
        2、跳转到添加成员页面
        3、填充正确的成员信息（姓名、账号、手机号），并保存
        4、跳转到通讯录页面，并返回姓名列表
        """
        with allure.step("进入到首页"):
            index = IndexPage(self.index.browser)
        with allure.step("在首页点击添加成员按钮，跳转到添加成员页面"):
            add_members = index.goto_add_members()
        with allure.step("填充成员信息（姓名、账号、手机号），并保存"):
            contact = add_members.add_member(name, acctid, phone)
        with allure.step("跳转到通讯录页面，并返回姓名列表"):
            name_list = contact.get_members()
        # 提前预断言判断
        if name not in name_list:
            # 浏览器截图
            path = self.index.SnapShot()
            # 将截图贴到报告中
            allure.attach.file(path, f"出错：'{name}' 不符合 {name_list}", attachment_type=allure.attachment_type.PNG)
        # 进行断言判断
        assert name in name_list

    # 设置测试用例参数化
    @pytest.mark.parametrize("name,acctid,phone,expect", get_case_data()[4], ids=get_case_data()[5])
    # 设置测试用例功能名
    @allure.feature("添加成员失败")
    # 设置测试用例执行顺序
    @pytest.mark.run(order=2)
    def test_add_members_fail(self, name, acctid, phone, expect):
        """
        添加成员测试用例失败
        1、在首页点击添加成员按钮
        2、跳转到添加成员页面
        3、填充错误的成员信息（姓名、账号、手机号），并返回获取的错误信息
        """
        with allure.step("进入到首页"):
            index = IndexPage(self.index.browser)
        with allure.step("在首页点击添加成员按钮，跳转到添加成员页面"):
            add_members = index.goto_add_members()
        with allure.step("填充错误的成员信息（姓名、账号、手机号），并返回错误信息"):
            tips = add_members.add_member_fail(name, acctid, phone, expect)
        # 提前预断言判断
        if expect not in tips:
            # 浏览器截图
            path = self.index.SnapShot()
            # 将截图贴到报告中
            allure.attach.file(path, f"出错：{expect} 不符合 {tips}", attachment_type=allure.attachment_type.PNG)
        # 进行断言判断
        assert expect in tips
