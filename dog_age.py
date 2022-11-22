dog_name = input("Sweet name of your pet is: ")
ok = 0
while True:
    try:
        h_age = int(input("Enter ther age of dog in human year: "))
    except:
        ok = 1
        print("please enter valid input")
    if ok == 1:
          continue  
    if h_age < 0:
        print("oops Age can not be in negative")
        break
    elif h_age >= 0:
        dog_age = ((h_age - 2)*4) + 10.5
        break
    

print(f"Age of your {dog_name} is {dog_age}")
