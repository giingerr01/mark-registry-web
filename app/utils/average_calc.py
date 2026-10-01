# average calculator


def calculate_average(marks):
    try:
        avg = sum(marks.values()) / len(marks)
    except ZeroDivisionError:
        avg = 0

    return avg
