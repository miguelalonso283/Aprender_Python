def run(items: list) -> list:
    result = []
    for x in items:
        if isinstance(x, list):
            result.extend(run(x))
        else:
            result.append(x)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
