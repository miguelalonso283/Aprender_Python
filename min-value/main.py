def run(values: list) -> int:
    result = values[0]
    for v in values[1:]:
        if v < result:
            result = v
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
