def sort(asc=True):
    def decorador(func):
        def wrapper(*args, **kwargs):
            return sorted(func(*args, **kwargs), reverse=not asc)
        return wrapper
    return decorador


# DO NOT TOUCH THE CODE BELOW
def run(asc, func, func_args) -> list:
    if isinstance(func_args, dict):
        return sort(asc)(func)(**func_args)
    return sort(asc)(func)(*func_args)


if __name__ == '__main__':
    import vendor

    vendor.launch(run)
