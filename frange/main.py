def run(start: float, stop: float, step: float) -> list:
    result = []
    n = 0
    while (v := start + n * step) < stop:
        result.append(v)
        n += 1
    return result



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
