def mcount(values: tuple, value: int = None) -> int:
    """Cuenta las apariciones de un valor en una tupla.

    :param values: tupla de números enteros.
    :type values: tuple
    :param value: valor a buscar (por defecto None).
    :type value: int
    :return: número de apariciones, o -1 si el valor es None.
    :rtype: int
    """
    if value is None:
        return -1
    total = 0
    for v in values:
        if v == value:
            total += 1
    return total


# DO NOT TOUCH THE CODE BELOW :-)
if __name__ == '__main__':
    import vendor

    vendor.launch(mcount)
