def assert_positive(func):
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()):
            if isinstance(value, (int, float)) and value <= 0:
                return None
        return func(*args, **kwargs)
    return wrapper


def run(func, func_args, func_kwargs):
    return assert_positive(func)(*func_args, **func_kwargs)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
