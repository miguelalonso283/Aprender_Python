def run(items: dict) -> bool:
    if not items:
        return True

    referencia = list(items.values())[0]

    for valor in items.values():
        if valor != referencia:
            return False

    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
