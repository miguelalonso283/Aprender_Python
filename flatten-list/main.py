def run(items: list) -> list:
    flatten_items = []
    for i in items:
        if not flatten_items or flatten_items[-1] != i:
            flatten_items.append(i)

    return flatten_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
