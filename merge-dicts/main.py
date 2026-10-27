def run(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    for i in d2:
        merged[i] = d2[i]
    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
