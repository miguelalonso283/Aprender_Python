def run(values: list) -> int:
    max_value = values[0]
    for v in values[1:]:
        if v > max_value:
            max_value = v
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
