#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    num_dict = {1: 'one', 2: 'two', 3: 'three'}
    print(num_dict)
    dict_items = num_dict.items()
    str_dict = {value: key for key, value in dict_items}
    print(str_dict)