def run(values: set) -> set:
    return {x // 2 for x in values} - values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
