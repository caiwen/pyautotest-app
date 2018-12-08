from src.gui.action.gb_login_action import GbLoginAction
from src.util.decorator import *
from test_suite_gb.test_case.test_base import BaseCase


class TestGbLogin(BaseCase):
    def setUp(self):
        super().setUp()
        self.device.app_start("com.globalegrow.app.gearbest")  # restart app

    def tearDown(self):
        super().tearDown()
        self.device.app_stop("com.globalegrow.app.gearbest")  # restart app

    @testcase
    def test_login(self):
        login_action = GbLoginAction(self.device)
        login_action.do_login()
