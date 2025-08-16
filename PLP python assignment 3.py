#question number 1
def calculate_discount(price,discount_percent):
    discount = price*discount_percent/100
    price_after_discount = price-discount
    if discount_percent >= 20:
        return price_after_discount
    else:
        return price
print(calculate_discount(4000, 30))
#question number 2
def calculate_discount(price,discount_percent):
    price = float(input("enter the price:"))
    discount_percent = float(input("enter the discount percent:"))
    discount = price*discount_percent/100
    price_after_discount = price-discount
    if discount_percent >= 20:
        return price_after_discount
    else:
        return price
print(calculate_discount(4000, 30))
