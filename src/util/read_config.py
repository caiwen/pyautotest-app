#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import approot


class ReadConfig:
    def __init__(self):
        self.file = '/config/config.ini'
        self.cf = configparser.ConfigParser()
        config_path = approot.get_root() + self.file
        self.cf.read(config_path, encoding='UTF-8')

    def get_method(self):
        value = self.cf.get("DEVICES", 'method')
        return value

    def get_server_url(self):
        value = self.cf.get("DEVICES", "server")
        return value

    def get_devices_ip(self):
        value = self.cf.get("DEVICES", "IP")
        return value.split('/')

    def get_apk_url(self):
        value = self.cf.get("APP", "apk_url")
        return value

    def get_apk_path(self):
        value = self.cf.get("APP", "apk_path")
        return value

    def get_pkg_name(self):
        value = self.cf.get("APP", "pkg_name")
        return value

    def get_testdata(self, name):
        value = self.cf.get("TESTDATA", name)
        return value.split('/')


if __name__ == '__main__':
    print(ReadConfig().get_pkg_name())
    print(ReadConfig().get_testdata('user_name'))
