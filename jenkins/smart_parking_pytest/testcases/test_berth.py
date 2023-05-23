import pytest
import os, sys
import logging
from conf.loadyaml import yamlload

sys.path.append(os.getcwd())
from action.action_berth import BerthProcess
from common.get_driver import Common
from common.public_login_ui import login


class TestBerth:

    def setup(self):
        # 调用登录
        login()
        logging.info('在用例执行前，调用了登录')

    def teardown(self):
        # 关闭浏览器
        Common.close_browser()
        logging.info('在用例执行后，调用了关闭浏览器')

    @pytest.mark.berth
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('data', yamlload('./data/berthdata.yaml'))
    def test_add_berth(self, data):
        number = data['number']
        logging.info(f'新增泊位中，获取到的泊位编号是：{number}')
        name = data['name']
        logging.info(f'新增泊位中，获取到的泊位名字是：{name}')
        text = BerthProcess().add_berth(number, name)
        logging.info(f'新增泊位中，获取到的提示文本是：{text}')
        print(text)
        assert text == '新增泊位成功'

    @pytest.mark.berth
    @pytest.mark.run(order=1)
    def test_del_berth(self):
        text = BerthProcess().del_berth()
        logging.info(f'删除泊位信息时获取到的提示文本是：{text}')
        print(text)
        assert text == '删除泊位成功'

    @pytest.mark.berth
    @pytest.mark.skip("测试pytest跳过功能")
    def test_skip(self):
        print('这是一个应该被跳过的用例')
        logging.error('如果执行到这里了，说明有问题哦')


if __name__ == '__main__':
    pytest.main(['--report=smark_parking.html',
                 '--title=郭凡の测试报告',
                 '--tester=fan',
                 '--desc=智慧泊车测试',
                 '--template=2'])
