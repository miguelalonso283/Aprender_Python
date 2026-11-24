def run(values: list) -> int:
    return -min(-v for v in values)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
