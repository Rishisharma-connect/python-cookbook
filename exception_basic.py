try:
    # 1 / 0
    print(b)
except (ZeroDivisionError, NameError):
    print('I got a ZeroDivisionError or Name Error')
