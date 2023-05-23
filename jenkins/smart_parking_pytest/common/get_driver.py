import os
import time
from telnetlib import EC

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Common:

    # 单例模式
    driver = None
    session = None


    # 打开浏览器
    @classmethod
    def get_driver(cls, browser_type ="edge"):
        if cls.driver is None:
            cpath = os.path.dirname(__file__)
            print(cpath)
            if browser_type == 'edge' or browser_type == 'gg':
                driver_path = os.path.join(os.path.dirname(cpath),
                                           r'driver/msedgedriver.exe')
                print(driver_path)
                cls.driver = webdriver.Edge(executable_path=driver_path)
            elif browser_type == 'firefox' or browser_type == 'ff':
                driver_path = os.path.join(os.path.dirname(cpath),
                                           'driver/geckodriver.exe')
                cls.driver = webdriver.Firefox(executable_path=driver_path)
            elif browser_type == "chrome" or browser_type == "goole":
                driver_path = os.path.join(os.path.dirname(cpath),
                                           'driver/chromedriver.exe')
                cls.driver = webdriver.Chrome(executable_path=driver_path)
            else:
                print("不是吧？这么多浏览器没有一个你能用的？QAQ")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        return cls.driver

    # 判断元素是否存在
    @classmethod
    def element_exist(cls, by, value):
        try:
            cls.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    # 显式等待
    @classmethod
    def wait_element_presence(cls, by, value, time_out=10):
        return WebDriverWait(cls.driver, time_out).until(lambda dr: dr.find_element(by, value))

    # 显示等待加强版（直接传入方法）
    @classmethod
    def wait_element_method(cls, method, time_out=5):
        return WebDriverWait(cls.driver, time_out).until(method)

    # 显示等待判断元素是否可见，如果可见就返回这个元素
    @classmethod
    def wait_element_EC(cls, by, value, time_out=10):
        return WebDriverWait(cls.driver, time_out).until(expected_conditions.visibility_of(cls.driver.find_element(by, value)))

    # 关闭浏览器
    @classmethod
    def close_browser(cls):
        cls.driver.quit()
        cls.driver = None

    # 接口：获取session
    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    # 接口：关闭session
    @classmethod
    def close_session(cls):
        cls.session.close()
        cls.session = None


