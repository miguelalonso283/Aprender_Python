def run(A: list, B: list, C: list) -> tuple:
    x = (A[0] + B[0] + C[0]) / 3
    y = (A[1] + B[1] + C[1]) / 3
    return round(x, 4), round(y, 4)

print(run([0, 0], [6, 0], [0, 6]))  # (2.0, 2.0)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
