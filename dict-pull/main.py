def run(data: dict, target_keys: tuple) -> dict:
    pdata = {k: v for k, v in data.items() if k in target_keys}
    return pdata


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
