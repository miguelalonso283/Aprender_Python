def run(cinfo: str) -> dict:
    cities = {}
    for bloque in cinfo.split(";"):
        if bloque == "":
            continue
        ciudad, poblacion = bloque.split(":")
        cities[ciudad] = int(poblacion)
    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
