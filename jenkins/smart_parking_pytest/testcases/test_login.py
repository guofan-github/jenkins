# coding:utf-8
import pytest
import os, sys

sys.path.append(os.getcwd())
from action.action_login import errorlogin, rightlogin
from conf.exceldata import Read
import logging


class TestLogin:
    """测试登录的测试用例"""

    @pytest.mark.login
    @pytest.mark.parametrize("user, pwd, code, msg", Read().get_data('登录测试数据', '登录测试'))
    def test_error_login(self, user, pwd, code, msg):
        # 执行登录操作
        errortext = errorlogin(user, pwd, code)
        logging.info(f'获取到的错误登录弹窗文本是：{errortext}')
        print(errortext)
        # 断言
        assert errortext == msg

    @pytest.mark.login
    def test_right_login(self):
        righttext = rightlogin()
        logging.info(f'获取到的正确登录弹窗文本是：{righttext}')
        print(righttext)
        assert righttext == '智慧泊车系统后台'


if __name__ == '__main__':
    pytest.main(['--report=smark_parking.html',
                 '--title=郭凡の测试报告',
                 '--tester=fan',
                 '--desc=智慧泊车登录测试',
                 '--template=2'])
