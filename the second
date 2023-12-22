#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from transport.trains import Train
from transport.sort_trains import sort_trains
from transport.find_destination import find_trains_by_destination

if __name__ == '__main__':
    # Создаем пустой список для хранения поездов
    trains = []

    # Ввод данных с клавиатуры
    n = int(input("Введите количество поездов: "))
    for i in range(n):
        destination = input("Введите название пункта назначения: ")
        train_number = input("Введите номер поезда: ")
        departure_time = input("Введите время отправления: ")
        train = Train(destination, train_number, departure_time)
        trains.append(train)

    # Сортировка списка по времени отправления поезда
    sort_trains(trains)

    # Вывод информации о поездах, направляющихся в указанный пункт назначения
    destination_input = input("Введите название пункта назначения: ")
    destination_trains = find_trains_by_destination(trains, destination_input)
    if destination_trains:
        for train in destination_trains:
            print(train)
    else:
        print("Поездов в указанный пункт назначения нет!")
