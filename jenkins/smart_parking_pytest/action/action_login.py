import os
import sys
import time

from selenium import webdriver

from common.get_driver import Common

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def errorlogin(user, pwd, code):
    driver = Common.get_driver()
    # 打开智慧泊车首页
    driver.get("http://192.168.163.131/smart_parking")

    # 用户名定位
    input_user = driver.find_element_by_css_selector('input[placeholder="请输入用户名"]')
    # 清除用户名输入框内文字
    input_user.clear()
    # 输入用户名
    time.sleep(1)
    input_user.send_keys(user)

    # 密码定位
    input_pwd = driver.find_element_by_css_selector('input[placeholder="请输入密码"]')
    # 清除密码输入框文字
    input_pwd.clear()
    # 输入密码
    time.sleep(1)
    input_pwd.send_keys(pwd)

    # 验证码定位
    input_code = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/form/div[3]/div/div[1]/input')
    # 清除验证码输入框文字
    input_code.clear()
    # 输入验证码
    time.sleep(1)
    input_code.send_keys(code)

    # 登录按钮定位
    loginbwn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/form/button[1]')
    # 点击登录按钮
    time.sleep(1)
    loginbwn.click()
    time.sleep(2)

    errtextlist = []
    # 错误提示
    errtext = driver.find_element_by_css_selector('body > div.el-overlay.is-message-box > div > '
                                                  'div.el-message-box__content > div.el-message-box__container > div '
                                                  '> p').text

    # 把每次的错误提示放进错误列表中
    errtextlist.append(errtext)

    # 关闭浏览器 释放资源
    Common.close_browser()

    # 把错误提示返回
    for errtext in errtextlist:
        if errtext != '' or errtext is not None:
            return errtext


def rightlogin():
    # 使用edge浏览器
    driver = Common.get_driver()
    # 打开智慧泊车首页
    driver.get("http://192.168.163.131/smart_parking")

    # 用户名定位
    input_user = driver.find_element_by_css_selector('input[placeholder="请输入用户名"]')
    # 清除用户名输入框内文字
    input_user.clear()
    # 输入用户名
    time.sleep(1)
    input_user.send_keys('gf')

    # 密码定位
    input_pwd = driver.find_element_by_css_selector('input[placeholder="请输入密码"]')
    # 清除密码输入框文字
    input_pwd.clear()
    # 输入密码
    time.sleep(1)
    input_pwd.send_keys('vvv333')

    # 验证码定位
    input_code = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/form/div[3]/div/div[1]/input')
    # 清除验证码输入框文字
    input_code.clear()
    # 输入验证码
    time.sleep(1)
    input_code.send_keys('0000')

    # 登录按钮定位
    loginbwn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/form/button[1]')
    # 点击登录按钮
    time.sleep(1)
    loginbwn.click()
    time.sleep(2)

    # 登录成功后的网站名
    success_text = driver.find_element_by_xpath('/html/body/div[1]/section/header/div[1]/h2').text

    # 关闭浏览器
    Common.close_browser()
    # 如果存在就返回
    if success_text:
        return success_text
