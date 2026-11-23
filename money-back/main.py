def run(to_give_back: float, available_currencies: list) -> dict | None:
    rest = round(to_give_back * 100)          # trabajamos en céntimos (evita errores de float)
    result = {}
    for c in sorted(available_currencies, reverse=True):
        n, rest = divmod(rest, round(c * 100))
        if n:
            result[c] = n
    return result if rest == 0 else None


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
