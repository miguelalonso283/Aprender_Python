def _proper_divisors(n: int):
    for d in range(1, n // 2 + 1):
        if n % d == 0:
            yield d

def is_perfect(n: int) -> bool:
    return n > 0 and sum(_proper_divisors(n)) == n

print(is_perfect(6))  # True
print(is_perfect(4))  # False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)
