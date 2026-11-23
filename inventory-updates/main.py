def run(imoves: str) -> dict:
    inventory = {}
    for m in imoves.split(','):
        item, amount = m[0], int(m[1:])
        inventory[item] = inventory.get(item, 0) + amount
    return inventory


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
