def run(items: dict) -> dict:
    return {''.join(k.split()): v for k, v in items.items()}


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
