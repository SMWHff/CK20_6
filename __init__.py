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
    try:
        os.system("cmd /C taskkill /f /im chromedriver.exe")
    finally:
        pytest.main(["-vs", "--alluredir", "./temp", "--clean-alluredir"])
        # allure generate ./temp -o ./report --clean
