def is_pangram(texto):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(texto.lower())


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)
