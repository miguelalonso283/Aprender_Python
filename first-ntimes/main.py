def run(numbers: list, nrep: int) -> int:
    counts = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    for n in numbers:                  # recorremos en orden para devolver el primero
        if counts[n] == nrep:
            return n
    return -1


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
