score = int(input("Please enter you score: "))

grade = score/10
ngrade = round(grade, 0)

if ngrade > 9:
    print(9)
elif ngrade < 1:
    print("Failed")
else:
    print(ngrade)