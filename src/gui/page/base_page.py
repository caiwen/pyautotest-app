import time
from uiautomator2 import UiObjectNotFoundError


class BasePage(object):
    def __init__(self, device):
        self.d = device

    def back(self):
        """点击返回
        页面没有加载完的时候，会出现返回失败的情况，使用前确认页面加载完成"""
        time.sleep(1)
        self.d.press('back')
        time.sleep(1)

    def identify(self):
        self.d.open_identify()

    def watch_device(self, keyword):
        """
        如果存在元素则自动点击
        :param keyword: exp: keyword="yes|允许|好的|跳过"
        """
        self.d.watchers.watched = False
        for i in keyword.split("|"):
            self.d.watcher(i).when(text=i).click(text=i)
        print('Starting watcher,parameter is %s' % keyword.split("|"))
        self.d.watchers.watched = True

    def unwatch_device(self):
        """关闭watcher """
        print('Stop all watcher')
        self.d.watchers.watched = False

    def get_toast_message(self):
        message = self.d.toast.get_message(3, 3)
        self.d.toast.reset()
        return message

    def set_fastinput_ime(self):
        self.d.set_fastinput_ime(True)

    def set_original_ime(self):
        self.d.set_fastinput_ime(False)

    @staticmethod
    def find_message(elements, text):
        """查找元素列表中是否存在 text"""
        count = elements.count
        while count > 0:
            count = count - 1
            message = elements[count].info['text']
            if text in message:
                return True
            elif count == 0:
                return False
        else:
            return False

    def _get_window_size(self):
        window = self.d.window_size()
        x = window[0]
        y = window[1]
        return x, y

    @staticmethod
    def _get_element_size(element):
        rect = element.info['bounds']
        x_center = (rect['left'] + rect['right']) / 2
        y_center = (rect['bottom'] + rect['top']) / 2
        x_left = rect['left']
        y_up = rect['top']
        x_right = rect['right']
        y_down = rect['bottom']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.d.swipe(fromX, fromY, toX, toY, steps)

    def swipe_up(self, element=None, steps=0.2):
        """
        swipe up
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)
            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.25 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=0.2):
        """
        swipe down
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.75 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_left(self, element=None, steps=0.2):
        """
        swipe left
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)
            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.25 * x
            toY = 0.5 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_right(self, element=None, steps=0.2):
        """
        swipe right
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)
            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.75 * x
            toY = 0.5 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def _find_element_by_swipe(self, direction, value, element=None, steps=0.2, max_swipe=6):
        """
        :param direction: swip direction exp: right left up down
        :param value: The value of the UI element location strategy. exp: d(text='Logina')
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: UI element
        """
        times = max_swipe
        for i in range(times):
            try:
                if value.exists:
                    return value
                else:
                    raise UiObjectNotFoundError
            except UiObjectNotFoundError:
                if direction == 'up':
                    self.swipe_up(element=element, steps=steps)
                elif direction == 'down':
                    self.swipe_down(element=element, steps=steps)
                elif direction == 'left':
                    self.swipe_left(element=element, steps=steps)
                elif direction == 'right':
                    self.swipe_right(element=element, steps=steps)
                if i == times - 1:
                    raise UiObjectNotFoundError

    def find_element_by_swipe_up(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('up', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_down(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('down', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_left(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('left', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_right(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('right', value,
                                           element=element, steps=steps, max_swipe=max_swipe)
