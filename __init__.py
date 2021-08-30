# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_6
# @File       : __init__.py
# @Time       : 2021/8/29 18:02
import os
import pytest

if __name__ == "__main__":
    # 启动测试用例，并清除旧报告，生成新的报告
    pytest.main(["-vs", "--alluredir", "./temp", "--clean-alluredir"])
    # 终端上输入 allure generate ./temp -o ./report --clean
