#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    workers = []
    while True:
        command = input(">>> ").lower()

        cmd_parts = command.split(maxsplit=1)
        match cmd_parts[0]:
            case 'exit':
                break
            case 'add':
                name = input('Введите фамилию и инициалы: ')
                post = input('Введите должность: ')
                year = int(input('Введите год поступления: '))
                workers.append({
                    'name': name,
                    'post': post,
                    'year': year
                })
                if len(workers) > 1:
                    workers.sort(key=lambda item: item.get('name', ''))
            case 'list':
                line = f'+-{"-" * 4}-+-{"-" * 30}-+-{"-" * 20}-+-{"-" * 8}-+'
                print(line)
                header = f"| {'№':^4} | {'Ф.И.О.':^30} | {'Должность':^20} | {'Год':^8} |"
                print(header)
                print(line)
                for index, worker in enumerate(workers, 1):
                    name, post, year = worker.get('name', ''), worker.get('post', ''), worker.get('year', 0)
                    recording = f"| {index:^4} | {name:^30} | {post:^20} | {year:^8} |"
                    print(recording)
                print(line)
            case 'select':
                today = date.today()
                period = int(cmd_parts[1])
                count = 0
                for worker in workers:
                    if today.year - worker.get('year', today.year) >= period:
                        count += 1
                        print(f'{count:^4}: {worker.get("name", "")}')
                if count == 0:
                    print('Работники с заданным стажем не найдены.')
            case 'help':
                print("Список команд:\n")
                print("add - добавить работника;")
                print("list - вывести список работников;")
                print("select <стаж> - запросить работников со стажем;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)
