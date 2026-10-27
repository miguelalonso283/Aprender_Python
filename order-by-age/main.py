def order_by_age(people: list) -> list:
    return sorted(people, key=lambda person: person['age'])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(order_by_age)
