def run(nums_dups: list) -> list:
    nums_unique = []

    for n in nums_dups:
        if n not in nums_unique:
            nums_unique.append(n)

    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
