def split_case(palabras):
    return ([p for p in palabras if p.islower()],
            [p for p in palabras if p.isupper()])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
