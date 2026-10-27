def cfreq(items, /, as_string=False):
    result = []
    if not items:
        return '' if as_string else []
    current = items[0]
    count = 1

    for item in items[1:]:
        if item == current:
            count += 1
        else:
            result.append((current,count))
            current = item
            count = 1
    result.append((current, count))
    if as_string:
        return ','.join(f'{elem}:{freq}' for elem, freq in result)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cfreq)
