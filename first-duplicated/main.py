def run(items: list) -> int | None:
    seen = set()
    for v in items:
        if v in seen:
            return v
        seen.add(v)
    return None


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
