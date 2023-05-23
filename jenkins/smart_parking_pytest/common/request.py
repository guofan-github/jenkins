import requests


class Call:

    def call(self, url, method, params=None, headers=None):
        # 将传入的method统统转换为小写，便于后续判断
        method = method.lower()

        # 将非get、post请求过滤掉，如后续有delete、put请求再加
        if method not in ('get', 'post'):
            raise Exception(f'暂未对该请求方式：{method}进行处理，后续将会优化')

        # 判断传入的是什么请求，调取对应封装函数
        if method == 'get':
            res = self.get(url, params, headers)
            return res.json()
        elif method == 'post':
            res = self.post(url, params, headers)
            return res.json()

        else:
            raise Exception('可你从不在灯火阑珊处')

    # 封装get请求
    def get(self, url, params, headers=None):
        # 获取get请求响应
        resp = requests.get(url, params=params, headers=headers)
        # 返回response
        return resp

    # 封装post请求
    def post(self, url, params, headers=None):
        # 获取post请求响应
        resp = requests.post(url, json=params, headers=headers)
        # 返回响应
        return resp
