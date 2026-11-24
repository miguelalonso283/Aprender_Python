def run(number: str) -> bool:
    # TODO
    return len(number) > 0 and all(c in '01' for c in number)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
