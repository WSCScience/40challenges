age = int(input("Please enter your age: "))

if age >= 13 and age <=15:
    print("30% discount")
elif age >= 16 and age <= 17:
    print("20% discount")
elif age >= 50:
    print("40% discount")
else:
    print("No discount")