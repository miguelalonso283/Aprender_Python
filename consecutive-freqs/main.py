def cfreq(items, /, salida=False) -> str | list:
    result = []
    if not items:
        return '' if salida else []
    
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
    if salida:
        return ','.join(f'{elem}:{freq}' for elem, freq in result)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cfreq)
