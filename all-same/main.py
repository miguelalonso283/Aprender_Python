def run(items: list) -> bool:
    return all(v == items[0] for v in items)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
