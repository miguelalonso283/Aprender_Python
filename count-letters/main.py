def run(text: str) -> dict:
    counter = {}
    for ch in text:
        counter[ch] = counter.get(ch, 0) + 1
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
