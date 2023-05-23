import time

# 定位层
from common.get_driver import Common


class BerthPage:

    def __init__(self):
        # 使用edge浏览器
        self.driver = Common.get_driver()

    # 定位路段管理
    def find_sections(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/aside/ul/div/div[1]/div/li['
                                                 '7]/div/span')

    # 定位泊位管理
    def find_berth(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/aside/ul/div/div[1]/div/li['
                                                 '7]/ul/li[3]/span')

    # 定位新增按钮
    def find_addbtn(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/button/span')

    # 定位泊位编号输入框
    def find_input_berthnumber(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/form/div[1]/div/div/input')

    # 定位泊位名称输入框
    def find_input_berthname(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/form/div[2]/div/div/input')

    # 定位地磁编号下拉框
    def find_geonumber(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/form/div[3]/div/div/div/div/input')

    # 定位地磁编号001
    def find_geonumber001(self):
        return self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/ul/li[1]')

    # 定位保存按钮
    def find_save(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/form/div[4]/div/button/span')

    # 定位新增成功弹窗
    def find_success_text(self):
        return self.driver.find_element_by_css_selector('div[class="el-notification__content"]')

    """这里是删除泊位定位"""

    # 定位删除按钮
    def find_delbtn(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button['
            '2]/span')

    # 定位确定删除按钮
    def find_delright(self):
        return self.driver.find_element_by_xpath('//div[@class="el-popconfirm__action"]/button[2]/span')

    # 定位删除成功弹窗
    def find_del_text(self):
        return self.driver.find_element_by_css_selector('#notification_1 > div > div > p')


# 操作层
class BerthAction(BerthPage):

    def __init__(self):
        BerthPage.__init__(self)

    # 点击路段管理
    def click_sections(self):
        self.find_sections().click()
        time.sleep(1)

    # 点击泊位管理
    def click_berth(self):
        self.find_berth().click()
        time.sleep(1)

    # 点击新增按钮
    def click_addbtn(self):
        self.find_addbtn().click()
        time.sleep(1.5)

    # 输入泊位编号
    def input_berthnumber(self, number):
        self.find_input_berthnumber().send_keys(number)

    # 输入泊位名称
    def input_berthname(self, name):
        self.find_input_berthname().send_keys(name)

    # 点击地磁编号下拉框
    def click_geonumber(self):
        self.find_geonumber().click()
        time.sleep(2)

    # 点击地磁编号001
    def click_geonumber001(self):
        self.find_geonumber001().click()
        time.sleep(1)

    # 点击保存按钮
    def click_save(self):
        self.find_save().click()
        time.sleep(1)

    # 获取成功弹窗文本
    def get_text(self):
        text = self.find_success_text().text
        return text

    # 点击删除按钮
    def click_delbtn(self):
        self.find_delbtn().click()
        time.sleep(2)

    # 点击删除确定
    def click_delright(self):
        self.find_delright().click()
        time.sleep(0.5)

    # 获取删除成功文本
    def get_del_text(self):
        text = self.find_del_text().text
        return text


# 业务层
class BerthProcess(BerthAction):

    def __init__(self):
        BerthAction.__init__(self)

    # 新增泊位业务流程
    def add_berth(self, number, name):
        # 点击路段管理
        self.click_sections()
        # 点击泊位管理
        self.click_berth()
        # 点击新增按钮
        self.click_addbtn()
        self.input_berthnumber(number)
        self.input_berthname(name)
        self.click_geonumber()
        self.click_geonumber001()
        self.click_save()
        msg = self.get_text()
        return msg

    # 删除泊位
    def del_berth(self):
        # 点击路段管理
        self.click_sections()
        # 点击泊位管理
        self.click_berth()
        # 点击删除按钮
        self.click_delbtn()
        # 点击确认删除
        self.click_delright()
        # 获取删除成功弹窗文本
        msg = self.get_del_text()
        return msg
