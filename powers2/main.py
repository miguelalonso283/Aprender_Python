def run(n: int) -> list:
    return [2 ** i for i in range(n + 1)]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
