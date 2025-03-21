
def calculate_discount(price, discount_percent):
    """calculates final price after applying discount"""
    if discount_percent >= 20:
        price = price - (price * (discount_percent/100))
        return price
    else:
        return price

original_price = float(input("Enter the original price of the product. "))
discount_percentage = float(input("Enter the percentage discount. "))

print(f"The final price after applying the discount is {calculate_discount(original_price, discount_percentage)}")