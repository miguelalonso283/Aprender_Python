def fibonacci(n):
    return _fib_aux(n, 0, 1)

def _fib_aux(n, a, b):
    if n == 0:
        return a
    return _fib_aux(n - 1, b, a + b)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(fibonacci)
