# A program that ask user to change Temprature value Fahrenheit to Celsius or Vise versa.
# It will ask until user type right value.
name: str = input("What is your good name dear? ")
degree = ""
ok = 0
while True:
    try:    
        temp = input("Enter the temperature you like to convert?(e.g., 45F, 102C, etc.: ")
        degree = int(temp[:-1])
        ok = 0
        
    except:
        ok = 1
        print("Enter a valid input")
    if ok == 1:
        continue
    i_convention = temp[-1]

    if i_convention.upper() == "C" :
        result = int(round((degree*9/5)+32))
        o_convention = "Fahrenheit"
        break
    elif i_convention.upper() == "F" :
        result = int(round((degree-32)*5/9))
        o_convention = "Celsius"
        break
    elif i_convention.upper() != "C" or i_convention.upper() != "F" :
        print(f"oops! You typed wrong keyword {name}, Type like 25C or 300F")
        

print("The temperature in" , o_convention, "is", result,"degrees.")

print(f"Thank you {name} for Your time . Have a good day dear {name}.")

