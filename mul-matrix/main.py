def run(a: list, b: list) -> list | None:
    if not a or not b or any(len(row) != len(b) for row in a):
        return None
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
