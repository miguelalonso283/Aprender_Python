def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    if age > 17 and age < 66 and weight > 50 and heartbeat > 49 and heartbeat < 111 and platelets > 150000:
        suitable_for_donation = True
    else:
        suitable_for_donation = False

    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
