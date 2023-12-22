#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from geometry import calculate_area

if __name__ == '__main__':
    # Вызов функции замыкания с параметром type = 0 для вычисления площади треугольника
    triangle_area = calculate_area(0)
    result_triangle = triangle_area(5, 10)
    print("Площадь треугольника:", result_triangle)

    # Вызов функции замыкания с параметром type = 1 для вычисления площади прямоугольника
    rectangle_area = calculate_area(1)
    result_rectangle = rectangle_area(5, 10)
    print("Площадь прямоугольника:", result_rectangle)
