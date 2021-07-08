try:
    1 / 0
except Exception:
    print('You can not divide by zero')
finally:
    print('Cleaning up')