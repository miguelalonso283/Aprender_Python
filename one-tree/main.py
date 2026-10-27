def run():
    num = 0

    for i in range(9):
        num += 10**i
        print(num**2)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
