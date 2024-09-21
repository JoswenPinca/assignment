price_1 = float(input("What is the price of your first purchase? "))
price_2 = float(input("What is the price of your second purchase? "))
price_3 = float(input("What is the price of your third purchase? "))

price_total = price_1 + price_2 + price_3

print("Current Total Cost: "+"₱{:.2f}".format(price_total))

if price_total>=100.00:
    print("10% Discount is applicable!")
    
    discount = price_total * 0.10
    discounted_total = price_total - discount
    loyalty_points = discounted_total / 10
    
    print(f"Discounted Price: "+"₱{:.2f}".format(discounted_total))
    print(f"Loyalty Points Earned: "+"{:.2f}".format(loyalty_points))
    
payment = float(input("Your payment? "))

if payment >= discounted_total:
    change = payment - discounted_total
    print(f"Payment Accepted! Your change is "+"₱{:.2f}".format(change))
else:
    print("Payment is lower than the price. Please try again!")