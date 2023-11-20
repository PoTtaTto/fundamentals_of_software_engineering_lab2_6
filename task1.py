#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1а': 30, '1б': 25,
        '2б': 30, '6а': 12,
        '7в': 5
    }
    print(school)

    # Изменение количество учащихся в классе 2б
    school['2б'] -= 3
    # Появление нового класса 11б в школе
    school['11б'] = 17
    # Расформирование 7в класса
    del school['7в']
    # Общее количество учащихся
    general_count = sum(school.values())

    print(school)