try:
    raise ImportError('Something happend')
except ImportError as err:
    print(type(err))
    print(err.args)
    print(err)