def run(n: int) -> str:
    if n == 0:
        return '0'
    bits = []
    while n > 0:
        bits.append(str(n % 2))   # resto de cada división sucesiva
        n //= 2
    bin_repr = ''.join(reversed(bits))
    return bin_repr

print(run(53))  # 110101
print(run(0))   # 0


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
