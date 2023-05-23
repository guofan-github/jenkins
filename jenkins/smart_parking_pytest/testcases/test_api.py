import logging

import openpyxl
import pytest
import requests

from common.public_api import token_save, send_request
from conf.exceldata import Read


class TestApi:

    # 测试开始前先进行登录，获取token
    def setup_class(self):
        print('++++++++++++++++++++++++++++++++++测试开始++++++++++++++++++++++++++++++++++')
        requests.get('http://192.168.163.131/smart_parking_bg/logout')
        token_save()

    # 数据驱动，同时测试多组数据，并将测试结果写入excel中
    @pytest.mark.api
    @pytest.mark.parametrize('data', Read().get_data('pytestAPI测试数据', 'API'))
    def test_api(self, data, request):
        # 获取接口请求参数
        id = data[0]
        method = data[1]
        logging.info(f'接口传入的方法为：{method}')
        url = data[2]
        logging.info(f'接口传入的url为：{url}')
        json = data[3]
        logging.info(f'接口传入的json为：{json}')
        headers = {'Authorization': f'{token_save()}'}
        logging.info(f'接口传入的请求头为：{headers}')
        res = send_request(method, url, json, headers)
        logging.info(f'实际获取响应为：{res},msg为：{res["msg"]}')
        expected = data[4]
        logging.info(f'期待值为：{expected}')
        # 断言
        try:
            assert res['msg'] == expected
            results = '测试通过'
        except Exception as e:
            results = '测试失败'
        # 写入excel测试结果列中
        file = openpyxl.load_workbook('./data/pytestAPI测试数据.xlsx')
        sheet = file['API']
        sheet.cell(id + 1, 6).value = results
        # 保存写入结果
        file.save('./data/pytestAPI测试数据.xlsx')


        def delete_department():
            if url == 'http://192.168.163.131/smart_parking_bg/department':
                resp = requests.get('http://192.168.163.131/smart_parking_bg/department')
                department_id = resp.json()['data']['list']
                id_list = []
                for i in department_id:
                    id_list.append(int(i['id']))
                max_id = max(id_list)
                logging.info(f'查到的最大id为：{max_id}')

                resp = requests.delete(f'http://192.168.163.131/smart_parking_bg/department/{max_id}')
                print(resp.json()['msg'])
                logging.info(f'删除department的id为：{max_id}，删除结果为{resp.json()["msg"]}')

        request.addfinalizer(delete_department)



if __name__ == '__main__':
    pytest.main(['-v', 'test_api.py'])
