import os
import time

import pyautogui
import pyperclip
import requests
import win32api
import win32con
from selenium.webdriver import ActionChains


class VerifyCode:
    def __init__(self, driver):
        self.driver = driver
        """ 目前这个接口时免费的。个人用没问题 """
        self.verify_url = "http://littlebigluo.qicp.net:47720/"

    def do_check(self):
        """ 保存图片到本地 """
        self.save_img()
        time.sleep(1)
        """ 选择验证码 """
        self.move()

    def save_img(self):
        ele = self.driver.find_element_by_class_name("loginImg")
        action = ActionChains(self.driver).move_to_element(ele)
        action.context_click(ele).perform()
        time.sleep(1)
        # 按v
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        """ 此文件路径要改成可配置，如果以后多用户，要考虑。 """
        pic = "D:\\Developer\\Code\\mydemo\\mysite\\test.jpg"
        pyperclip.copy(pic)
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "V")
        """ 回车前，先把这个目录下的图片清理 """
        if os.path.exists(pic):
            os.remove(pic)
            time.sleep(1)
        pyautogui.press("enter")

    def upload_img(self):
        """ rb 以二进制方式读该文件 """
        response = requests.post(self.verify_url, files={"pic_xxfile": open("test.jpg", "rb")})
        time.sleep(2)
        num = response.text.split("<B>")[1].split("<")[0]
        print('验证码识别成功！图片位置：%s' % num)
        try:
            if int(num):
                return [int(num)]
        except ValueError:
            num = list(map(int, num.split()))
            return num

    def move(self):
        """ 调用接口上传返回结果 """
        num = self.upload_img()
        try:
            ele = self.driver.find_element_by_class_name('loginImg')
            for i in num:
                if i <= 4:
                    ActionChains(self.driver).move_to_element_with_offset(ele, 40 + 72 * (i - 1), 73).click().perform()
                else:
                    i -= 4
                    ActionChains(self.driver).move_to_element_with_offset(ele, 40 + 72 * (i - 1), 145).click().perform()
        except:
            print('元素不可选!')
