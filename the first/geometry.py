def calculate_area(type=0):
    def inner_function(x, y):
        if type == 0:
            area = 0.5 * x * y
        else:
            area = x * y
        return area

    return inner_function
