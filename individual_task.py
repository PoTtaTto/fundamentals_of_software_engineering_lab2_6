#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import randint


if __name__ == '__main__':
    trains = []
    while True:
        cmd = input('>>> ')
        cmd_parts = cmd.split(maxsplit=1)
        match cmd_parts[0]:
            case 'add':
                train_num = int(input('Введите номер поезда: '))
                destination = input('Введите пункт назначения: ')
                start_time = input('Введите время выезда: ')
                trains.append({'num': train_num, 'destination': destination, 'start_time': start_time})
                if len(trains) > 1:
                    trains.sort(key=lambda item: item['start_time'])
            case 'list':
                line = f'+-{"-" * 15}-+-{"-" * 30}-+-{"-" * 25}-+'
                print(line)
                header = f"| {'№ поезда':^15} | {'Пункт назначения':^30} | {'Время отъезда':^25} |"
                print(header)
                print(line)
                for train in trains:
                    num = train.get('num', randint(1000, 10000))
                    destination = train.get('destination', 'None')
                    start_time = train.get('start_time', 'None')
                    recording = f"| {num:^15} | {destination:^30} | {start_time:^25} |"
                    print(recording)
                print(line)
            case 'select':
                cmd_destination = cmd_parts[1]
                select_trains = [train for train in trains if train['destination'] == cmd_destination]
                if len(select_trains) > 1:
                    for train in select_trains:
                        print(f'{train["num"]:^15}: {train["start_time"]:^25}')
                else:
                    print('Нет поездов едущих в данное место!', file=sys.stderr)
            case 'help':
                print("Список команд:\n")
                print("add - добавить поезд;")
                print("list - вывести список поездов;")
                print("select <пункт назначения> - запросить поезда с пунктом назначения;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            case 'exit':
                break
            case _:
                print(f"Неизвестная команда {cmd}", file=sys.stderr)