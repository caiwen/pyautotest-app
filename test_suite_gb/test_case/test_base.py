"""
测试用例的基类
"""
import unittest
from bootstrap.bootstrap import Bootstrap
from src.util import constants


class BaseCase(unittest.TestCase):
    def setUp(self):
        Bootstrap()
        self.device = constants.get_value('device')

    def tearDown(self):
        self.device = None


if __name__ == '__main__':
        unittest.main()
