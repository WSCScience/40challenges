time = int(input("Please enter how long you spend watching TV a day: "))

if time <= 2:
    print("That should be ok")
elif time > 2 and time <= 4:
    print("That will rot your brain")
else:
    print("That is too much TV")