def run(stock: dict, merch: str, amount: int) -> bool:
    return stock.get(merch, 0) >= amount


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
