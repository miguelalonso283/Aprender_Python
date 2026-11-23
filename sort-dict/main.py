def run(unsorted_items: dict) -> list[tuple]:
    return sorted(unsorted_items.items(), key=lambda t: t[1])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
