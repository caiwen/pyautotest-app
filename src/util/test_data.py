#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from src.util.read_config import ReadConfig
import approot
data_path = approot.get_root() + '/data/data.json'


def generate_test_data(devices):
    dict_tmp = {}
    for d in devices:
        print(d['udid'])
        dict_tmp[d['serial']] = {}
        dict_tmp[d['serial']]['user_name'] = ReadConfig().get_testdata('user_name')[devices.index(d)]
        dict_tmp[d['serial']]['password'] = ReadConfig().get_testdata('password')[devices.index(d)]
    with open(data_path, "w") as f:
        json.dump(dict_tmp, f, ensure_ascii=False)
        f.close()
    print("Test data data.json generated success")


def get_test_data(d):
    # with open(data_path, 'r', encoding='UTF-8') as f: #mac
    with open(data_path, 'r') as f:
        data = json.load(f)
    print(d.device_info['serial'])
    return data[d.device_info['serial']]
