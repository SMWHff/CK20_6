# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : contact_page.py
# @Time       : 2021/8/29 15:39
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object.base_page import BasePage


class ContactPage(BasePage):
    """
    通讯录页面
    """
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    _member_name = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _member_phone = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
    _delete = (By.CSS_SELECTOR, ".js_delete")
    _accept = (By.XPATH, "//a[text()='确认']")
    _tips = (By.ID, "js_tips")

    def goto_add_members(self):
        """
        跳转到添加成员页面
        :return: 返回通讯录页面对象实例
        """
        # 防止循环引用对象实例，需要在方法内部进行包导入操作
        from page_object.add_members_page import AddMembersPage
        return AddMembersPage(self.browser)

    def del_member(self, phone):
        """
        删除成员操作
        :param phone: 手机号
        :return: 返回提示内容
        """
        # 查找符合条件的成员勾选框
        ele = self.find(By.XPATH, f"//*[@title='{phone}']/../td[1]/input")
        # 判断该成员是否被勾选
        if not ele.is_selected():
            # 未勾选，则勾选该成员
            ele.click()
        # 点击【删除】按钮
        self.find(self._delete).click()
        # 点击【确认】按钮
        self.find(self._accept).click()
        # 显示等待 6 秒，每隔 0.5 秒进行一次判断是否删除完毕
        # 如果找不到“正在删除...”，则表示删除操作完毕
        WebDriverWait(self, 6).until_not(lambda x: self.find(self._tips).text == "正在删除...")
        result = self.find(self._tips).text
        return result

    def get_members(self):
        """
        返回成员列表
        :return: 返回姓名列表
        """
        # 创建姓名列表
        name_list = []
        # 查找所有成员姓名元素，返回元素列表
        ele_list = self.finds(self._member_name)
        # 遍历列表中的每个元素
        for ele in ele_list:
            # 将元素中的文本内容放进姓名列表中
            name_list.append(ele.text)
        # 返回姓名列表
        return name_list

    # def del_member(self, phone):
    #     """
    #     删除成员操作
    #     :param phone: 手机号
    #     :return: 返回提示内容
    #     """
    #     # 查找符合条件的成员勾选框
    #     ele = self.find(By.XPATH, f"//*[@title='{phone}']/../td[1]/input")
    #     # 判断该成员是否被勾选
    #     if not ele.is_selected():
    #         # 未勾选，则勾选该成员
    #         ele.click()
    #     # 点击【删除】按钮
    #     self.find(self._delete).click()
    #     # 点击【确认】按钮
    #     self.find(self._accept).click()
    #     try:
    #         #显示等待 6 秒，每间隔 0.5 秒判断一次是否删除成功
    #         tips = self.find(self._tips).text
    #         print("显示等待 6 秒，返回提示内容：", tips)
    #         WebDriverWait(self, 6).until_not(lambda x:x.find(x._tips).text == "正在删除...")
    #         tips = self.find(self._tips).text
    #     except Exception as e:
    #        #否则，返回提示内容
    #        for i in range(10):
    #            tips = self.find(self._tips).text
    #            sleep(1)
    #            print("否则，返回提示内容：", tips)
    #     return tips


if __name__ == "__main__":
    contact = ContactPage()
    print(contact.del_member("15578805343"))
