
import requests

# 因为网站有token，封装每次登录的token
def token_save():
    url = "http://192.168.163.131/smart_parking_bg/login"
    json = {"accountName":"gf","password":"vvv333","captcha":"0000","captchaKey":"0000"}
    res = requests.post(url, json=json)
    token = res.json()
    return token["msg"]

# 封装函数，方法、url、json数据
def send_request(method, url, json, head):
    # 判断
    if method=="get":
        res = requests.get(headers=head, url=url, data=json)
    elif method=="post":
        js = eval(json)
        res = requests.post(headers=head, url=url, json=js)
    elif method=="delete":
        res = requests.delete(headers=head, url=url, json=json)
    return res.json()

if __name__ == '__main__':
    a = token_save()
    print(a)