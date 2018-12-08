from src.util.drivers import Drivers
from src.util import constants
from src.util.test_data import *
import uiautomator2 as u2


class Bootstrap(object):
    def __init__(self):
        devices = Drivers().get_devices()
        constants._init()
        # generate test data data.json 准备测试数据
        generate_test_data(devices)
        constants.set_value('app_devices', devices)
        if 'ip' in devices[0]:
            dri = devices[0]['ip']
        else:
            dri = devices[0]['serial']

        constants.set_value('device', u2.connect(dri))
