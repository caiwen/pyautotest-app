#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2 as u2
from time import sleep
from src.gui.page.base_page import BasePage
from src.util.decorator import *


class GbLoginPage(BasePage):

    def __init__(self, device):
        BasePage.__init__(self, device)
        try:
            self.d(resourceId="com.globalegrow.app.gearbest:id/tv_cancel",
                   className="android.widget.TextView").click()
            print("弹窗:TextView，后点击：Not now")
        except u2.UiObjectNotFoundError as reason:
            print('没弹窗:TextView')
        finally:
            self.d(text="Account").click()
        self.d(text="SIGN IN").click()

    def wait_page(self):
        try:
            if self.d(resourceId="com.globalegrow.app.gearbest:id/btn_login").wait(timeout=15):
                return True
            else:
                raise Exception('Not in LoginPage')
        except Exception:
            raise Exception('Not in LoginPage')

    @teststep
    def input_username(self, text):
        self.d(resourceId="com.globalegrow.app.gearbest:id/et_login_username") \
            .set_text(text)

    @teststep
    def input_password(self, text):
        self.d(resourceId="com.globalegrow.app.gearbest:id/et_login_password") \
            .set_text(text)

    @teststep
    def login_click(self):
        self.d(resourceId="com.globalegrow.app.gearbest:id/btn_login").click()

    @teststep
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.login_click()
        sleep(2)
