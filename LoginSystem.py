import time

from selenium import webdriver

from VerifyCode import VerifyCode


class LoginSystem:
    def __init__(self, username, password, login_url):
        self.username = username
        self.password = password
        self.login_url = login_url

    def login(self):
        driver.get(self.login_url)
        """ 停止2秒等待页面加载完毕 """
        time.sleep(2)
        """ 获取12306登录页的tab账号登录 """
        account_login_btn = driver.find_element_by_class_name("login-hd-account")
        """ 点击切换到账号登录tab """
        account_login_btn.click()
        time.sleep(2)
        """ 获取用户名密码输入框设置值 """
        driver.find_element_by_id("J-userName").send_keys(self.username)
        driver.find_element_by_id("J-password").send_keys(self.password)
        """ 获取验证码模块，选择验证码 """
        vc = VerifyCode(driver)
        vc.do_check()
        """ 点击登录按钮 """
        driver.find_element_by_id("J-login").click()

    def main(self):
        self.login()


if __name__ == '__main__':
    beginTime = time.time()
    """ 获取驱动 """
    driver = webdriver.Chrome("chrome driver的位置，后续改成可配置")
    """ 最大化窗口 """
    driver.maximize_window()
    """ 登录初始化信息 """
    ls = LoginSystem("***你的12306账号***", "***你的12306密码***", "https://kyfw.12306.cn/otn/resources/login.html")
    ls.main()
    # driver.quit()
