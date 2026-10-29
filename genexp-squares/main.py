def gen_sq(n: int):
    return (i ** 2 for i in range(n))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(gen_sq)
