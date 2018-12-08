from .base_action import BaseAction
from ..page.gb_login_page import GbLoginPage
from src.util.decorator import *


class GbLoginAction(BaseAction):
    @teststeps
    def do_login(self):
        loginPage = GbLoginPage(self.d)
        loginPage.wait_page()
        loginPage.set_fastinput_ime()
        loginPage.login('aaaa', 'bbb')
        print('登录成功')
