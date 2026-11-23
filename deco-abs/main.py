def fabs(func):
    def wrapper(a, b, *args):
        return func(abs(a), abs(b), *args)
    return wrapper

# DO NOT TOUCH THE CODE BELOW
def run(func, func_args):
    return fabs(func)(*func_args)


if __name__ == '__main__':
    import vendor

    vendor.launch(run)
