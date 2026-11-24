def run(items: list) -> list:
    return [v for i, v in enumerate(items) if i == 0 or v != items[i - 1]]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
