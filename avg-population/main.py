def run(pdata: dict) -> dict:
    total = sum(v for v in pdata.values())
    avg_data = {k: round(v*100 / total,3) for k, v in pdata.items()}
    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
