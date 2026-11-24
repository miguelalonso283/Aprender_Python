def run(input: tuple) -> tuple[set, set]:
    return ({p[0] for p in input}, {p[1] for p in input})


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
