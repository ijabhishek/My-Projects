
# electricity and wter bill 
electricity_bill_amount = float(input("Enter the total electricity bill amount: "))
water_bill_amount = float(input("Enter the amount of water bill: "))
other_expanses = float(input("Enter if any other expanses occured:"))
# bill reading of tenants
amit_bill_reading = int(input("Bill reading of Amit: "))
mirtunjay_bill_reading = int(input("Bill reading of Mirtunjay: "))
abhishek_bill_reading = int(input("Bill reading of Abhishek: "))
motar_bill_reading = int(input("Bill reading of water motar: "))


total_bill_reading = amit_bill_reading + mirtunjay_bill_reading + abhishek_bill_reading + motar_bill_reading

avg_bill_amount = electricity_bill_amount / total_bill_reading

motar_bill_amount_perperson = (avg_bill_amount*motar_bill_reading)/3

amit_bill_amount = (amit_bill_reading*avg_bill_amount) + (water_bill_amount/3) + (other_expanses/3) + motar_bill_amount_perperson
mirtunjay_bill_amount = (mirtunjay_bill_reading*avg_bill_amount) + (water_bill_amount/3) + (other_expanses/3) + motar_bill_amount_perperson
abhishek_bill_amount = (abhishek_bill_reading*avg_bill_amount) + (water_bill_amount/3) + (other_expanses/3) + motar_bill_amount_perperson

print(f"Average bill amount: {avg_bill_amount}")
print(f"Motar bill amount per person: {motar_bill_amount_perperson}")
print(f"Bill amounts of all tenants :\n Amit's bill total amount is {amit_bill_amount} \n Mirtunjay'bill amount is {mirtunjay_bill_amount} \n Abhisehk's bill Amount is {abhishek_bill_amount}")


