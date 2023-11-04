price_square_metter = 7.61
square_metters = float(input())
#discount 18%

total_area = square_metters*price_square_metter
discount = 18*total_area/100
price_to_pay = total_area - discount

print(f"The final price is {price_to_pay} lv.")
print(f"The discount is {discount} lv.")